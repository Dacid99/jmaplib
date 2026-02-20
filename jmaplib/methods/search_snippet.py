from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, ClassVar

from dataclasses_json import config

from jmaplib import constants

if TYPE_CHECKING:
    from jmaplib.models import EmailQueryFilter, ListOrRef, SearchSnippet, TypeOrRef

from jmaplib.methods.base import Get, GetResponseWithoutState


class SearchSnippetBase:
    method_namespace: str | None = "SearchSnippet"
    using: ClassVar[set[str]] = {constants.JMAP_URN_MAIL}


@dataclass
class SearchSnippetGet(SearchSnippetBase, Get):
    ids: ListOrRef[str] | None = field(
        metadata=config(field_name="emailIds"), default=None
    )
    filter: TypeOrRef[EmailQueryFilter] | None = None


@dataclass
class SearchSnippetGetResponse(SearchSnippetBase, GetResponseWithoutState):
    data: list[SearchSnippet] = field(metadata=config(field_name="list"))
