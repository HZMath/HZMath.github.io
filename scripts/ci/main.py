"""
Script for Pull Request Actions.

When PR:
- opened: add a comment, label the PR, check and report plugins
- synchronize: update plugin report if plugin changed
- closed: congratulate if merged
- labeled: regenerate plugin report if labeled with `recheck`

Reports:
- `reporter.report` reports the result to standard output and workflow summary
- `utilities.report_all` and `gh_cli.pr_comment` reports the result to PR comment

Environ:
- EVENT_TYPE: utilities.EventType
- IS_MERGED: bool

---

This file is part of scripts of MCDReforged Plugin Catalogue.

This is a free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License,
or (at your option) any later version.

This is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
in the `scripts` folder of the project root. If not, see
<https://www.gnu.org/licenses/>.
"""

import asyncio
import logging
import os
import sys
from pathlib import Path
from typing import Optional

# Make import and script runs from correct directory
# See also: https://github.com/MCDReforged/PluginCatalogue/pull/268#issuecomment-1555874245
sys.path.append("scripts")

import gh_cli as gh
from common.logger import logger
from utils import Action, ActionList, EventType, Tag, get_changed

# ---- Gather environs and constants ---- #
# See also: .github/workflows/pull_request.yml

POST_CHECK_LIMIT = 16
COMMENT_USER = "github-actions"
RECHECK_LABEL = "recheck"

EVENT_TYPE = EventType(os.environ.get("EVENT_TYPE"))
IS_MERGED = os.environ.get("IS_MERGED", "false")

MSG_MERGED_FIRST = """
{},

Congratulations on your first merged contribution! 🎉✨
Thank you for joining the community — your PR is now a part of our website!

We’re thrilled to welcome you as a contributor and hope to see more from you in the future!
Welcome aboard, and happy coding! 🚀
""".strip()

FIRST_TIME_HEADER = """
**Hi, {}!**  
This is your first contribution to our website. Welcome! 🎉  

To ensure a smooth review process, please:  
- 📖 **Read the [Contribution Guidelines](https://github.com/HZMath/HZMath.github.io/blob/master/CONTRIBUTING.md)** (if you haven’t already).  
- 🔍 **Check existing plugins** for reference on formatting and metadata.

There will be a deploy preview generated for your changes.
If you’ve added/modified articles, a report will be generated below.
- ✅ **Verify your changes** by reading the report.

We’ll review your PR soon — thanks for your patience!
Hope you have a great day!
""".strip()

MSG_HEADER = """
Thanks for your contribution! 🎉
Please be patient before we done checking. If you've added or modified articles, a brief report will be generated below.
Have a nice day!
""".strip()

# MSG_CHECKLIST = '''
#
# ```markdown
# # 合并前检查单（供仓库维护者参考）
# - *插件适合提交；
# - 提交者有权提交；
# - 所提交信息完整有效；
# - 插件分类正确，名称、介绍和说明符合要求。
# 详见贡献指南
# ```
# '''

logger.setLevel(logging.INFO)

# ---- On closed ---- #
if EVENT_TYPE == EventType.CLOSED and IS_MERGED == "true":  # merged
    author, is_first_time = gh.check_contributor()
    if is_first_time:
        gh.pr_comment(
            MSG_MERGED_FIRST.format(f"@{author}" if author else "Contributor")
        )
    sys.exit(0)

# ---- No limit on recheck ---- #
if EVENT_TYPE == EventType.LABELED:
    POST_CHECK_LIMIT = 0

# ---- Gather file changes ---- #
# https://github.com/marketplace/actions/changed-files#outputs-

logger.info(f"Running with event type: {EVENT_TYPE}")
logger.info("Gathering changed files")

# Add, Copied, Modified, Renamed, Deleted
added_files = set(get_changed("added_files"))  # A
deleted_files = set(get_changed("deleted_files"))  # D
all_files = set(get_changed("all_changed_files"))  # ACMRD

# This is a workaround for `lots0logs/gh-action-get-changed-files`
# See https://github.com/MCDReforged/PluginCatalogue/issues/524
all_files = all_files.union(deleted_files)

logger.info(f"{len(all_files)} changes found")

# ---- Identify actions and tags ---- #
# In order of priority, the process should be:
# 1. A(CMR)D of `plugins/<plugin_id>/plugin_info.json` == AMD of plugin
# 2. ACMRD of `plugins/<plugin_id>/**` == Modify of plugin
# 3. ACMRD of `scripts/**` == `scripts`
# 4. ACMRD of `.github/workflows/**` == `github workflow`
# One plugin should only have one action.

logger.info("Identifying actions and tags")

actions: ActionList = ActionList()

# search Markdown file
for file in sorted(all_files, key=lambda x: x.endswith(".md"), reverse=True):
    path = Path(file).parts
    if len(path) > 1 and path[0] == "content":

        post = path[-2]
        if path[-1] == "index.md":  # for directory post
            if file in added_files:
                actions.add(Action(Tag.ARTICLE_ADD, post))
            elif file in deleted_files:
                actions.add(Action(Tag.ARTICLE_REMOVE, post))
            else:
                actions.add(Action(Tag.ARTICLE_MODIFY, post))


logger.info(f'Identified actions: {", ".join(map(str, actions))}')
logger.info(f'Identified labels: {", ".join(map(str, actions.labels))}')

# ---- Run plugin checks and generate report ---- #

report: Optional[str] = None

if actions.posts:
    modified_posts = actions.modified_posts
    removed_posts = actions.removed_posts
    plugin_list = []
    reached_limit = False
    if modified_posts:
        logger.info(f'Checking posts: {", ".join(modified_posts)}')
        reporter.record_script_start()
        reporter.record_command("pr_check")
        if len(modified_posts) > POST_CHECK_LIMIT > 0:
            logger.warning(f"Too many posts to check (>{POST_CHECK_LIMIT}), skipping")
            reached_limit = True
            reporter.record_script_failure(report, ValueError(report))
        else:
            plugin_list = get_plugin_list(modified_plugins)
            asyncio.run(plugin_list.fetch_data(fail_hard=False, skip_release=False))
            reporter.report(plugin_list)
    report = report_all(
        plugin_list, actions, removed_plugins, reached_limit=reached_limit
    )
else:
    logger.info("No plugins to report, skipping")

# ---- Label and comment ---- #

if EVENT_TYPE == EventType.OPENED:
    author, is_first_time = gh.check_contributor()

    reply = (
        FIRST_TIME_HEADER.format(f"@{author}" if author else "Contributor")
        if is_first_time
        else MSG_HEADER
    )

    gh.pr_label(add_labels=sorted(actions.labels))
    gh.pr_comment(reply)

if EVENT_TYPE == EventType.LABELED:
    gh.pr_label(remove_labels=[RECHECK_LABEL])

if report:
    gh.pr_update_or_comment(COMMENT_USER, report)

if len(reporter.failures) > 0:
    logger.error(f"Plugin check reported {len(reporter.failures)} failures.")
    sys.exit(1)
