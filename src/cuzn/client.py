from typing import Optional

import requests
from dotenv import load_dotenv

from .config import ConfigItem, get_config_value
from .errors import ConfigurationError
from .session import BrazeSession


class BrazeClient:

    __slots__ = ["__endpoint__", "__api_key__", "__timeout__", "__session__"]

    def __init__(
        self,
        *,
        braze_endpoint: Optional[str] = None,
        braze_api_key: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> None:
        load_dotenv()  # load environment variables from .env file

        self.__endpoint__ = braze_endpoint or get_config_value(ConfigItem.API_ENDPOINT)
        self.__api_key__ = braze_api_key or get_config_value(ConfigItem.API_KEY)
        self.__timeout__ = timeout or get_config_value(ConfigItem.API_TIMEOUT)

        self._validate_config()

    def create(self) -> BrazeSession:
        """
        Create and return the configured client session
        """

        self._validate_config()

        self.__session__ = requests.Session()
        self.__session__.headers.update(
            {
                "Authorization": f"Bearer {self.__api_key__}",
                "Content-Type": "application/json",
            }
        )

        return BrazeSession(session=self.__session__)

    def _validate_config(self) -> None:
        """
        Validate the instance configuration. Raises a `ConfigurationError` exception if
        the validation fails.
        """

        try:
            assert self.__endpoint__ is not None
            assert self.__api_key__ is not None
        except AssertionError:
            raise ConfigurationError("Could not configure a Braze client")
