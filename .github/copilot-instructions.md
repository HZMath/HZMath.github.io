# Copilot instructions for HZMath/HZMath.github.io

Purpose: help Copilot sessions understand how to build, run, and contribute to this Hugo-based site and follow repository-specific conventions.

Build, test, and lint commands
- Local development server: `hugo server -D` (serve drafts with -D). Opens at http://localhost:1313 by default.
- Full production build: `hugo` (outputs into `public/`). Netlify uses the same command (see netlify.toml: build.command = "hugo").
- Preview a single change: run `hugo server -D` and open the URL for the changed page under `/`.
- Tests/lint: repository has no automated unit test suite. CI optionally lists `python-frontmatter` in pyproject.toml for front-matter checks — to run similar checks locally, install `python-frontmatter` and run any CI/utility scripts present in `scripts/`.

High-level architecture (big picture)
- Static website built with Hugo (theme in `archetypes/` and a theme dependency in `go.mod`).
- Content is under `content/` (subsections: `post`, `external`, etc.). `content/external` is the canonical place for community-submitted articles.
- Site assets (images, CSS, JS) live under `assets/` and `static/` depending on whether they are processed by Hugo Pipes.
- `public/` contains the generated site (do not edit manually).
- `config/` holds Hugo configuration files; Netlify config is in `netlify.toml` (deploys using `hugo` and sets HUGO_VERSION).
- CI may run lightweight Python checks (see `pyproject.toml` optional deps).

Key repository conventions
- Contribution flow: follow `CONTRIBUTING.md`. Submit articles via Pull Requests; submissions must be placed in `content/external`.
- PR requirements: PR title for article submissions should start with `[Article]`. Use the provided PR template and ensure its checkboxes are completed before request for review.
- Front Matter: use the archetype template (`archetypes/post.md`) for required front-matter fields. The `license` field is auto-filled if left empty (per CONTRIBUTING.md).
- One PR per article when publishing; multiple-file edits allowed for non-article changes.
- Use `hugo-extended` locally if you need image processing features; otherwise `hugo` is sufficient for builds matching Netlify's environment.
- Theme and copyright: see `theme_copyright_info/README.md` for theme attribution details.

AI / assistant notes for future Copilot sessions
- 始终用中文回复本仓库相关的问题与说明。
- When asked to modify content, check `content/external` and `archetypes/post.md` for front-matter expectations.
- Avoid editing files in `public/` — changes should be made to source content/config instead.
- Look at `netlify.toml` for deploy settings and `pyproject.toml` for CI-related Python tooling.
- If validating front matter or metadata, prefer repository scripts (in `scripts/`) or `python-frontmatter` rather than inventing new checks.

Files to consult when making changes
- README.md — repository overview
- CONTRIBUTING.md — contribution rules and PR expectations
- archetypes/post.md — front-matter template
- netlify.toml — build/deploy instructions
- config/ and assets/ — site configuration and resources

MCP servers
- (Optional) For web preview automation (Playwright), ask the maintainer before configuring. If requested, a Playwright server can be added to validate rendered pages.

If this file should be expanded or tuned (e.g., include specific CI script names or local dev requirements), say which area to enhance.
