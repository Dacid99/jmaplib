import functools
import json

import responses


def assert_request_return_response(
    expected_request,
    response,
):
    def _response_callback(
        expected_request,
        response,
        request,
    ):
        assert request.headers["Content-Type"] == "application/json"
        assert json.loads(request.body or "{}") == expected_request
        return (200, {}, json.dumps(response))

    return functools.partial(_response_callback, expected_request, response)


def expect_jmap_call(
    http_responses,
    expected_request,
    response,
):
    response.setdefault("sessionState", "test;session;state")
    http_responses.add_callback(
        method=responses.POST,
        url="https://jmap-api.localhost/api",
        callback=assert_request_return_response(expected_request, response),
    )
