from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, ClassVar

from dataclasses_json import config

from jmaplib import constants
from jmaplib.methods.base import (
    Changes,
    ChangesResponse,
    Copy,
    CopyResponse,
    Get,
    GetResponse,
    Import,
    ImportResponse,
    Query,
    QueryChanges,
    QueryChangesResponse,
    QueryResponse,
    Set,
    SetResponse,
)

if TYPE_CHECKING:
    from jmaplib.models import Email, EmailQueryFilter, SetError
    from jmaplib.models import EmailImport as EmailImportModel


class EmailBase:
    method_namespace: str | None = "Email"
    using: ClassVar[set[str]] = {constants.JMAP_URN_MAIL}


@dataclass
class EmailChanges(EmailBase, Changes):
    pass


@dataclass
class EmailChangesResponse(EmailBase, ChangesResponse):
    pass


@dataclass
class EmailCopy(EmailBase, Copy):
    create: dict[str, Email] | None = None


@dataclass
class EmailCopyResponse(EmailBase, CopyResponse):
    created: dict[str, Email] | None = None


@dataclass
class EmailGet(EmailBase, Get):
    body_properties: list[str] | None = None
    fetch_text_body_values: bool | None = None
    fetch_html_body_values: bool | None = field(
        metadata=config(field_name="fetchHTMLBodyValues"), default=None
    )
    fetch_all_body_values: bool | None = None
    max_body_value_bytes: int | None = None


@dataclass
class EmailGetResponse(EmailBase, GetResponse):
    data: list[Email] = field(metadata=config(field_name="list"))


@dataclass
class EmailImport(EmailBase, Import):
    emails: dict[str, EmailImportModel] = field(default_factory=dict)


@dataclass
class EmailImportResponse(EmailBase, ImportResponse):
    created: dict[str, Email] | None = None
    not_created: dict[str, SetError] | None = field(
        metadata=config(field_name="notCreated"), default=None
    )


@dataclass
class EmailQuery(EmailBase, Query):
    filter: EmailQueryFilter | None = None
    collapse_threads: bool | None = None


@dataclass
class EmailQueryResponse(EmailBase, QueryResponse):
    pass


@dataclass
class EmailQueryChanges(EmailBase, QueryChanges):
    filter: EmailQueryFilter | None = None
    collapse_threads: bool | None = None


@dataclass
class EmailQueryChangesResponse(EmailBase, QueryChangesResponse):
    pass


@dataclass
class EmailSet(EmailBase, Set):
    create: dict[str, Email] | None = None


@dataclass
class EmailSetResponse(EmailBase, SetResponse):
    created: dict[str, Email | None] | None
    updated: dict[str, Email | None] | None
