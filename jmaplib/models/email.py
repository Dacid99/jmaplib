from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Final, Union

from dataclasses_json import config

from jmaplib.serializer import Model, datetime_decode, datetime_encode

if TYPE_CHECKING:
    from datetime import datetime

    from .models import EmailAddress, ListOrRef, Operator, StrOrRef


@dataclass
class Email(Model):
    id: str | None = field(metadata=config(field_name="id"), default=None)
    blob_id: str | None = None
    thread_id: str | None = None
    mailbox_ids: dict[str, bool] | None = None
    keywords: dict[str, bool] | None = None
    size: int | None = None
    received_at: datetime | None = field(
        default=None,
        metadata=config(encoder=datetime_encode, decoder=datetime_decode),
    )
    message_id: list[str] | None = None
    in_reply_to: list[str] | None = None
    references: list[str] | None = None
    headers: list[EmailHeader] | None = None
    mail_from: list[EmailAddress] | None = field(
        metadata=config(field_name="from"), default=None
    )
    to: list[EmailAddress] | None = None
    cc: list[EmailAddress] | None = None
    bcc: list[EmailAddress] | None = None
    reply_to: list[EmailAddress] | None = None
    subject: str | None = None
    sent_at: datetime | None = field(
        default=None,
        metadata=config(encoder=datetime_encode, decoder=datetime_decode),
    )
    body_structure: EmailBodyPart | None = None
    body_values: dict[str, EmailBodyValue] | None = None
    text_body: list[EmailBodyPart] | None = None
    html_body: list[EmailBodyPart] | None = None
    attachments: list[EmailBodyPart] | None = None
    has_attachment: bool | None = None
    preview: str | None = None


@dataclass
class EmailHeader(Model):
    name: str | None = None
    value: str | None = None


@dataclass
class EmailBodyPart(Model):
    part_id: str | None = None
    blob_id: str | None = None
    size: int | None = None
    headers: list[EmailHeader] | None = None
    name: str | None = None
    type: str | None = None
    charset: str | None = None
    disposition: str | None = None
    cid: str | None = None
    language: list[str] | None = None
    location: str | None = None
    sub_parts: list[EmailBodyPart] | None = None


@dataclass
class EmailBodyValue(Model):
    value: str | None = None
    is_encoding_problem: bool | None = None
    is_truncated: bool | None = None


@dataclass
class EmailQueryFilterCondition(Model):
    in_mailbox: StrOrRef | None = None
    in_mailbox_other_than: ListOrRef[str] | None = None
    before: datetime | None = field(
        default=None,
        metadata=config(encoder=datetime_encode, decoder=datetime_decode),
    )
    after: datetime | None = field(
        default=None,
        metadata=config(encoder=datetime_encode, decoder=datetime_decode),
    )
    min_size: int | None = None
    max_size: int | None = None
    all_in_thread_have_keyword: StrOrRef | None = None
    some_in_thread_have_keyword: StrOrRef | None = None
    none_in_thread_have_keyword: StrOrRef | None = None
    has_keyword: StrOrRef | None = None
    not_keyword: StrOrRef | None = None
    has_attachment: bool | None = None
    text: StrOrRef | None = None
    mail_from: str | None = field(metadata=config(field_name="from"), default=None)
    to: StrOrRef | None = None
    cc: StrOrRef | None = None
    bcc: StrOrRef | None = None
    body: StrOrRef | None = None
    header: ListOrRef[str] | None = None


@dataclass
class EmailQueryFilterOperator(Model):
    operator: Operator
    conditions: list[EmailQueryFilter]


@dataclass
class EmailImport(Model):
    """Represents an Email to be imported via the Email/import JMAP method."""

    blob_id: str = field(metadata=config(field_name="blobId"))
    mailbox_ids: dict[str, bool] = field(metadata=config(field_name="mailboxIds"))
    keywords: dict[str, bool] | None = None
    received_at: datetime | None = field(
        default=None,
        metadata=config(
            encoder=datetime_encode,
            decoder=datetime_decode,
            field_name="receivedAt",
        ),
    )


class EmailProperties:
    """Property keys of an email object.

    References:
        https://jmap.io/spec-mail.html#properties-of-the-email-object
    """

    ID: Final[str] = "id"
    BLOB_ID: Final[str] = "blobId"
    THREAD_ID: Final[str] = "threadId"
    MAILBOX_IDS: Final[str] = "mailboxIds"
    KEYWORDS: Final[str] = "keywords"
    SIZE: Final[str] = "size"
    RECEIVED_AT: Final[str] = "receivedAt"
    MESSAGE_ID: Final[str] = "messageId"
    IN_REPLY_TO: Final[str] = "inReplyTo"
    REFERENCES: Final[str] = "references"
    SENDER: Final[str] = "sender"
    FROM: Final[str] = "from"
    TO: Final[str] = "to"
    CC: Final[str] = "cc"
    BCC: Final[str] = "bcc"
    REPLY_TO: Final[str] = "replyTo"
    SUBJECT: Final[str] = "subject"
    SENT_AT: Final[str] = "sentAt"
    BODY_STRUCTURE: Final[str] = "bodyStructure"
    BODY_VALUES: Final[str] = "bodyValues"
    TEXT_BODY: Final[str] = "textBody"
    HTML_BODY: Final[str] = "htmlBody"
    ATTACHMENTS: Final[str] = "attachments"
    HAS_ATTACHMENT: Final[str] = "hasAttachment"
    PREVIEW: Final[str] = "preview"


class EmailBodyPartProperties:
    """Property keys of an email bodypart object.

    References:
        https://jmap.io/spec-mail.html#properties-of-the-email-object
    """

    PART_ID: Final[str] = "partId"
    BLOB_ID: Final[str] = "blobId"
    SIZE: Final[str] = "size"
    HEADERS: Final[str] = "headers"
    NAME: Final[str] = "name"
    TYPE: Final[str] = "type"
    CHARSET: Final[str] = "charset"
    DISPOSITION: Final[str] = "disposition"
    CID: Final[str] = "cid"
    LANGUAGE: Final[str] = "language"
    LOCATION: Final[str] = "location"
    SUB_PARTS: Final[str] = "subParts"


EmailQueryFilter = Union[EmailQueryFilterCondition, EmailQueryFilterOperator]
