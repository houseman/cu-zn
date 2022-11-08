import pytest


def test_init_not_configurable():
    from cuzn.client import Client
    from cuzn.errors import ConfigurationError

    with pytest.raises(ConfigurationError):
        Client()


def test_envvar_fallback(mocker):
    import os

    from cuzn.client import Client

    env = {"CUZN_BRAZE_ENDPOINT": "https://abc.xyz", "CUZN_BRAZE_API_KEY": "foobar"}

    mocker.patch.dict(os.environ, env)

    client = Client()

    assert client._endpoint == env["CUZN_BRAZE_ENDPOINT"]
    assert client._api_key == env["CUZN_BRAZE_API_KEY"]


def test_explicit_config():
    from cuzn.client import Client

    CUZN_BRAZE_ENDPOINT = "https://abc.xyz"
    CUZN_BRAZE_API_KEY = "foobar"

    client = Client(
        braze_endpoint=CUZN_BRAZE_ENDPOINT, braze_api_key=CUZN_BRAZE_API_KEY
    )

    assert client._endpoint == CUZN_BRAZE_ENDPOINT
    assert client._api_key == CUZN_BRAZE_API_KEY
