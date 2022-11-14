import pytest


def test_init_not_configurable(mocker):
    import os

    from cuzn import client as module
    from cuzn.client import BrazeClient
    from cuzn.errors import ConfigurationError

    env = {}
    mocker.patch.dict(os.environ, env)
    mocker.patch.object(module, "load_dotenv")

    with pytest.raises(ConfigurationError):
        BrazeClient()


def test_envvar_fallback(mocker):
    import os

    from cuzn.client import BrazeClient

    env = {"CUZN_BRAZE_ENDPOINT": "https://abc.xyz", "CUZN_BRAZE_KEY": "foobar"}
    mocker.patch.dict(os.environ, env)

    client = BrazeClient()

    assert client._endpoint == env["CUZN_BRAZE_ENDPOINT"]
    assert client._api_key == env["CUZN_BRAZE_KEY"]


def test_explicit_config():
    from cuzn.client import BrazeClient

    CUZN_BRAZE_ENDPOINT = "https://abc.xyz"
    CUZN_BRAZE_KEY = "foobar"

    client = BrazeClient(
        braze_endpoint=CUZN_BRAZE_ENDPOINT, braze_api_key=CUZN_BRAZE_KEY
    )

    assert client._endpoint == CUZN_BRAZE_ENDPOINT
    assert client._api_key == CUZN_BRAZE_KEY


def test_create(mocker):
    from cuzn.client import BrazeClient

    CUZN_BRAZE_ENDPOINT = "https://abc.xyz"
    CUZN_BRAZE_KEY = "foobar"

    client = BrazeClient(
        braze_endpoint=CUZN_BRAZE_ENDPOINT, braze_api_key=CUZN_BRAZE_KEY
    ).create()

    assert client._session.headers["Authorization"] == f"Bearer {CUZN_BRAZE_KEY}"
    assert client._session.headers["Content-Type"] == "application/json"
