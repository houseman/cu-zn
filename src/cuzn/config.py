import os
from enum import Enum
from typing import Optional, TypeVar, Union

_T = TypeVar("_T", bound=Union[int, str])


class ConfigItem(Enum):
    """
    Enum value of Tuple[str, Callable[[_T], Type[_T]]]
    """

    API_ENDPOINT = ("CUZN_BRAZE_ENDPOINT", str)
    API_KEY = ("CUZN_BRAZE_KEY", str)
    API_TIMEOUT = ("CUZN_BRAZE_TIMEOUT", int)


def get_config_value(config_item: ConfigItem) -> Optional[_T]:
    """
    Return an environment variable value for the given key (cast to key type, else
    `None` if no environment variable value is set for the key.
    """

    key, type_callable = config_item.value
    env_val = os.getenv(key)
    if not env_val:
        return None

    return type_callable(env_val)
