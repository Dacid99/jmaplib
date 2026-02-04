from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Union

from dataclasses_json import config

from jmaplib.serializer import Model

if TYPE_CHECKING:
    from .models import Operator, StrOrRef


@dataclass
class Mailbox(Model):
    id: str | None = field(metadata=config(field_name="id"), default=None)
    name: str | None = None
    sort_order: int | None = 0
    total_emails: int | None = None
    unread_emails: int | None = None
    total_threads: int | None = None
    unread_threads: int | None = None
    is_subscribed: bool | None = False
    role: str | None = None
    parent_id: str | None = field(metadata=config(field_name="parentId"), default=None)


@dataclass
class MailboxQueryFilterCondition(Model):
    name: StrOrRef | None = None
    role: StrOrRef | None = None
    parent_id: StrOrRef | None = None
    has_any_role: bool | None = None
    is_subscribed: bool | None = None


@dataclass
class MailboxQueryFilterOperator(Model):
    operator: Operator
    conditions: list[MailboxQueryFilter]


MailboxQueryFilter = Union[MailboxQueryFilterCondition, MailboxQueryFilterOperator]
