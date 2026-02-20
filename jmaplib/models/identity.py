from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from jmaplib.serializer import Model

if TYPE_CHECKING:
    from jmaplib.models.models import EmailAddress


@dataclass
class Identity(Model):
    name: str
    email: str
    reply_to: str | None
    bcc: list[EmailAddress] | None
    text_signature: str | None
    html_signature: str | None
    may_delete: bool
    id: str | None = None
