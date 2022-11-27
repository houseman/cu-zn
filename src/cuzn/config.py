import os
from typing import Dict, Optional

from dotenv import load_dotenv


class Config:
    __data__: Dict[str, Optional[str]] = {}

    def __init__(self) -> None:
        if not self.__data__:
            self._load_env_vars()

    def get_str(self, key: str, default_value: Optional[str] = None) -> Optional[str]:
        """
        Return a configuration string value, for the given key name.
        If no value is found, return `default_value`, or `None`
        """

        value = self.__data__.get(key)
        if value is None:
            return default_value

        return str(value)

    def get_int(self, key: str, default_value: Optional[int] = None) -> Optional[int]:
        """
        Return a configuration integer value, for the given key name.
        If no value is found, return `default_value`, or `None`
        """

        value = self.__data__.get(key)
        if value is None:
            return default_value
        try:
            return int(value)
        except ValueError:
            return default_value

    def _load_env_vars(self) -> None:
        """
        Load environment variables that have key prefix "CUZN_" into the `__data__`
        class variable.

        Variable key-value pairs are loaded from the `.env` file, if this exists.
        """

        load_dotenv()  # load environment variables from .env file
        self.__data__ = {
            k.upper(): v for k, v in os.environ.items() if k.upper().startswith("CUZN_")
        }
