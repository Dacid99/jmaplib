from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import TYPE_CHECKING, Any

import pytest
from dataclasses_json import config

from jmaplib import EmailHeader, ResultReference

if TYPE_CHECKING:
    from jmaplib.models import ListOrRef
from jmaplib.serializer import Model, datetime_decode, datetime_encode


def test_camel_case():
    @dataclass
    class TestModel(Model):
        camel_case_key: str

    d = TestModel(camel_case_key="fourside")
    to_dict = d.to_dict()
    assert to_dict == dict(camelCaseKey="fourside")
    from_dict = TestModel.from_dict(to_dict)
    assert from_dict == d


def test_serialize_result_reference():
    @dataclass
    class TestModel(Model):
        ids: ListOrRef[str]

    d = TestModel(
        ids=ResultReference(
            name="Some/method",
            path="/ids",
            result_of="method0",
        ),
    )
    to_dict = d.to_dict()
    assert to_dict == {
        "#ids": {"name": "Some/method", "path": "/ids", "resultOf": "method0"}
    }


def test_serialize_header():
    @dataclass
    class TestModel(Model):
        headers: list[EmailHeader]

    d = TestModel(
        headers=[
            EmailHeader(name="name", value="value"),
        ],
    )
    to_dict = d.to_dict()
    assert to_dict == {
        "header:name": "value",
    }


def test_serialize_header_2():
    @dataclass
    class TestModel(Model):
        headers: list[EmailHeader]

    d = TestModel(
        headers=[
            EmailHeader(name="name", value="value"),
        ],
    )
    to_dict = d.to_dict()
    assert to_dict == {
        "header:name": "value",
    }


def test_serialize_add_account_id():
    @dataclass
    class TestModel(Model):
        account_id: str | None = field(init=False)
        data: str

    d = TestModel(
        data="is beautiful",
    )
    to_dict = d.to_dict(account_id="u1138")
    assert to_dict == dict(accountId="u1138", data="is beautiful")


@pytest.mark.parametrize(
    ["dt", "expected_dict"],
    [
        (
            datetime(2022, 2, 26, 12, 31, 45, tzinfo=timezone.utc),
            dict(timestamp="2022-02-26T12:31:45Z"),
        ),
        (None, {}),
    ],
)
def test_serialize_datetime(dt, expected_dict):
    @dataclass
    class TestModel(Model):
        timestamp: datetime | None = field(
            default=None,
            metadata=config(encoder=datetime_encode, decoder=datetime_decode),
        )

    d = TestModel(timestamp=dt)
    to_dict = d.to_dict()
    assert to_dict == expected_dict
    from_dict = TestModel.from_dict(to_dict)
    assert from_dict == d
