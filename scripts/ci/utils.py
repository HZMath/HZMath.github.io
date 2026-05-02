import json
from enum import Enum
from typing import Iterable, Optional

from common.constants import REPOS_ROOT


class EventType(Enum):
    """Workflow event types that script accepts"""

    OPENED = "opened"
    SYNCHRONIZE = "synchronize"
    LABELED = "labeled"
    CLOSED = "closed"


class Tag(str, Enum):
    """Issue (PR) tags"""

    ARTICLE_ADD = "article add"
    ARTICLE_MODIFY = "article modify"
    ARTICLE_REMOVE = "article remove"
    CI = "CI/CD"
    SCRIPTS = "scripts"

    @property
    def label(self) -> str:
        """Pull request label name from tags

        All post changes labels `posts`
        """
        if self in (self.ARTICLE_ADD, self.ARTICLE_MODIFY, self.ARTICLE_REMOVE):
            return "article"
        return self.value  # type: ignore


class Action:
    """PR actions"""

    tag: Tag
    post: Optional[str]

    def __init__(self, tag: Tag, post: str | None = None):
        self.tag = tag
        self.post = post

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Action):
            return self.tag == value.tag and self.post == value.post
        return False

    def __hash__(self) -> int:
        return hash((self.tag, self.post))

    def __str__(self) -> str:
        return f"[{self.tag.value}]" + f"({self.post})" if self.post else ""

    def __repr__(self) -> str:
        return self.__str__()


class ActionList(set[Action]):
    """PR Action list with a [post, tag] dict"""

    posts: dict[str, Tag]

    def __init__(self) -> None:
        super().__init__()
        self.posts = {}

    def add(self, action: Action) -> None:
        super().add(action)
        if action.post:
            self.posts[action.post] = action.tag

    @property
    def tags(self) -> set[Tag]:
        """Returns all tags of actions"""
        return {action.tag for action in self}

    @property
    def labels(self) -> set[str]:
        """Returns all labels of actions"""
        return {tag.label for tag in self.tags}

    @property
    def modified_posts(self) -> list[str]:
        """Returns all modified posts"""
        return [
            post
            for post, tag in self.posts.items()
            if tag in (Tag.ARTICLE_ADD, Tag.ARTICLE_MODIFY)
        ]

    @property
    def removed_posts(self) -> list[str]:
        """Returns all removed posts"""
        return [post for post, tag in self.posts.items() if tag == Tag.ARTICLE_REMOVE]

    @property
    def post_ids(self) -> Iterable[str]:
        """Returns all post ids of actions"""
        return self.posts.keys()


def get_changed(change_type: str) -> list[str]:
    with open(
        REPOS_ROOT / f".github/outputs/{change_type}.json", "r", encoding="utf8"
    ) as f:
        return json.load(f)
