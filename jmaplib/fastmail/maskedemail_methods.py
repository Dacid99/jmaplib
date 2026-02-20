from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, ClassVar

from dataclasses_json import config

from jmaplib.methods.base import Get, GetResponse, Set, SetResponse

if TYPE_CHECKING:
    from jmaplib.fastmail.maskedemail_models import MaskedEmail

URN = "https://www.fastmail.com/dev/maskedemail"


class MaskedEmailBase:
    method_namespace: str | None = "MaskedEmail"
    using: ClassVar[set[str]] = {URN}


@dataclass
class MaskedEmailGet(MaskedEmailBase, Get):
    pass


@dataclass
class MaskedEmailGetResponse(MaskedEmailBase, GetResponse):
    data: list[MaskedEmail] = field(metadata=config(field_name="list"))


@dataclass
class MaskedEmailSet(MaskedEmailBase, Set):
    pass


@dataclass
class MaskedEmailSetResponse(MaskedEmailBase, SetResponse):
    created: dict[str, MaskedEmail | None] | None
    updated: dict[str, MaskedEmail] | None
