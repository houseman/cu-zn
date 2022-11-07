import pytest


def test_init_not_configurable():
    from cuzn.client import Client

    with pytest.raises(Exception):
        Client()
