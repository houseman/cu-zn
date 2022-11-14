import pytest

from cuzn.config import ConfigItem


@pytest.mark.parametrize(
    ["env", "config_item", "expected"],
    [
        ({"CUZN_BRAZE_ENDPOINT": "foobar"}, ConfigItem.API_ENDPOINT, "foobar"),
        ({"CUZN_BRAZE_TIMEOUT": "30"}, ConfigItem.API_TIMEOUT, 30),
        ({"CUZN_BRAZE_KEY": ""}, ConfigItem.API_KEY, None),
    ],
)
def test_get_config_value(mocker, env, config_item, expected):
    import os

    from cuzn.config import get_config_value

    mocker.patch.dict(os.environ, env)

    output = get_config_value(config_item)

    assert output == expected
