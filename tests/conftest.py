from __future__ import annotations

import json
import logging
import tempfile
import time
from pathlib import Path

import pytest
import responses

from jmaplib import Client
from jmaplib.logging import log
from tests.data import make_session_response

pytest.register_assert_rewrite("tests.data", "tests.utils")


@pytest.fixture(autouse=True)
def test_log():
    class UTCFormatter(logging.Formatter):
        converter = time.gmtime

    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = UTCFormatter(
        "%(asctime)s %(name)-12s %(levelname)-8s "
        "[%(filename)s:%(funcName)s:%(lineno)d] %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    log.setLevel(logging.DEBUG)


@pytest.fixture
def client():
    return Client(host="jmap-example.localhost", auth=("ness", "pk_fire"))


@pytest.fixture
def http_responses_base():
    with responses.RequestsMock() as resp_mock:
        yield resp_mock


@pytest.fixture
def http_responses(
    http_responses_base,
):
    http_responses_base.add(
        method=responses.GET,
        url="https://jmap-example.localhost/.well-known/jmap",
        body=json.dumps(make_session_response()),
    )
    return http_responses_base


@pytest.fixture
def tempdir():
    with tempfile.TemporaryDirectory(suffix=".unit_test") as td:
        yield Path(td)
