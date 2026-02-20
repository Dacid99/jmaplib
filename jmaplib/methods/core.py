from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from jmaplib import constants
from jmaplib.methods.base import Method, Response


class CoreBase:
    method_namespace: str | None = "Core"
    using: ClassVar[set[str]] = {constants.JMAP_URN_CORE}


class EchoMethod:
    method_type: str | None = "echo"


@dataclass
class CoreEcho(CoreBase, EchoMethod, Method):
    def to_dict(self, *args: Any, **kwargs: Any) -> dict[str, Any]:
        return self.data or {}

    data: dict[str, Any] | None = None


@dataclass
class CoreEchoResponse(CoreBase, EchoMethod, Response):
    data: dict[str, Any] | None = None

    @classmethod
    def from_dict(cls, kvs: Any, *args: Any, **kwargs: Any) -> CoreEchoResponse:
        return CoreEchoResponse(data=kvs)
