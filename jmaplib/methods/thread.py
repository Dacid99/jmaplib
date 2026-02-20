from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, ClassVar

from dataclasses_json import config

from jmaplib import constants
from jmaplib.methods.base import Changes, ChangesResponse, Get, GetResponse

if TYPE_CHECKING:
    from jmaplib.models import Thread


class ThreadBase:
    method_namespace: str | None = "Thread"
    using: ClassVar[set[str]] = {constants.JMAP_URN_MAIL}


@dataclass
class ThreadChanges(ThreadBase, Changes):
    pass


@dataclass
class ThreadChangesResponse(ThreadBase, ChangesResponse):
    pass


@dataclass
class ThreadGet(ThreadBase, Get):
    pass


@dataclass
class ThreadGetResponse(ThreadBase, GetResponse):
    data: list[Thread] = field(metadata=config(field_name="list"))
