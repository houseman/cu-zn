import pytest


@pytest.mark.parametrize(
    ["env", "key", "default_value", "expected"],
    [
        (
            {"CUZN_FOO": "foobar"},
            "CUZN_FOO",
            None,
            "foobar",
        ),
        (
            {"cuzn_foo": "foobar"},
            "CUZN_FOO",
            None,
            "foobar",
        ),  # This works, but rather don't use lowercase key names
        (
            {"CUZN_BAR": "30"},
            "CUZN_BAR",
            None,
            "30",
        ),
        (
            {"FOO_BAR": "foobar"},
            "FOOBAR",
            None,
            None,
        ),  # Needs the "CUZN_" prefix
        (
            {},
            "CUZN_FOOBAR",
            "foobar",
            "foobar",
        ),  # Default value given
    ],
)
def test_get_str(mocker, env, key, default_value, expected):
    mocker.patch.dict("os.environ", env, clear=True)
    from cuzn.config import Config

    print(f"Config().__data__: {Config().__data__}")
    output = Config().get_str(key=key, default_value=default_value)

    assert output == expected


@pytest.mark.parametrize(
    ["env", "key", "default_value", "expected"],
    [
        (
            {"CUZN_BAR": "30"},
            "CUZN_BAR",
            None,
            30,
        ),
        (
            {"cuzn_bar": "30"},
            "CUZN_BAR",
            None,
            30,
        ),  # This works, but rather don't use lowercase key names
        (
            {"CUZN_FOO": "foobar"},
            "CUZN_FOO",
            None,
            None,
        ),  # `ValueError`, returns `None`
        (
            {"CUZN_BAR": "30.5"},
            "CUZN_BAR",
            None,
            None,
        ),  # This also raises a `ValueError`
        (
            {"FOO_BAR": "100"},
            "FOOBAR",
            None,
            None,
        ),  # Needs the "CUZN_" prefix
        (
            {},
            "CUZN_BAR",
            100,
            100,
        ),  # `default_value` given
    ],
)
def test_get_int(mocker, env, key, default_value, expected):
    mocker.patch.dict("os.environ", env, clear=True)
    from cuzn.config import Config

    print(f"Config().__data__: {Config().__data__}")
    output = Config().get_int(key=key, default_value=default_value)

    assert output == expected
