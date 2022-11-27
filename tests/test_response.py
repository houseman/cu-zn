import pytest


@pytest.mark.parametrize(
    ["code", "expected"],
    [
        (200, True),  # 200 OK
        (204, True),  # 204 No Content
        (400, False),  # 400 Bad Request
        (429, False),  # 429 Too Many Requests
        (500, False),  # 500 Internal Server Error
        (503, False),  # 503 Service Unavailable
        (100, False),  # 100 Continue
        (301, False),  # 301 Moved Permanently
    ],
)
def test_is_success(mocker, code, expected):
    from cuzn.response import BrazeResponse

    response = BrazeResponse(code=code, content=mocker.Mock(), request=mocker.Mock())

    assert response.is_success() == expected


@pytest.mark.parametrize(
    ["code", "expected"],
    [
        (200, False),  # 200 OK
        (204, False),  # 204 No Content
        (400, True),  # 400 Bad Request
        (429, True),  # 429 Too Many Requests
        (500, True),  # 500 Internal Server Error
        (503, True),  # 503 Service Unavailable
        (100, False),  # 100 Continue
        (301, False),  # 301 Moved Permanently
    ],
)
def test_is_error(mocker, code, expected):
    from cuzn.response import BrazeResponse

    response = BrazeResponse(code=code, content=mocker.Mock(), request=mocker.Mock())

    assert response.is_error() == expected


@pytest.mark.parametrize(
    ["content", "expected"],
    [
        (None, {}),
        ("None", {}),
        ("[[}}", {}),
        ('{"foo": "bar"}', {"foo": "bar"}),
    ],
)
def test_payload(mocker, content, expected):
    from cuzn.response import BrazeResponse

    response = BrazeResponse(code=200, content=content, request=mocker.Mock())

    assert response.payload == expected


def test_payload_memoisation(mocker):
    import ujson

    from cuzn.response import BrazeResponse

    data = {"foo": "bar"}
    content = ujson.dumps(data)
    response = BrazeResponse(code=200, content=content, request=mocker.Mock())

    assert response.__payload__ is None
    assert response.payload.get("bar") is None
    assert response.__payload__ == data
    assert response.payload.get("foo") == "bar"


@pytest.mark.parametrize(
    ["code", "expected"],
    [
        (200, "BrazeResponse<200>"),
        (400, "BrazeResponse<400>"),
        (500, "BrazeResponse<500>"),
    ],
)
def test_repr(mocker, code, expected):
    from cuzn.response import BrazeResponse

    response = BrazeResponse(code=code, content="", request=mocker.Mock())

    assert f"{response}" == expected


def test_immutability(mocker):
    from cuzn.response import BrazeResponse

    response = BrazeResponse(code=201, content="foo", request=mocker.Mock())
    assert response.code == 201
    assert response.content == "foo"

    with pytest.raises(AttributeError):
        # Trying to set a property value should raise an AttributeError
        response.content = "bar"
