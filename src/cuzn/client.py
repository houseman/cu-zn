from typing import Optional

import requests

from .config import Config
from .errors import ConfigurationError
from .session import BrazeSession


class BrazeClient:
    def __init__(
        self,
        *,
        braze_endpoint: Optional[str] = None,
        braze_api_key: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> None:

        self.__endpoint__ = braze_endpoint or Config().get_str("CUZN_BRAZE_ENDPOINT")
        self.__api_key__ = braze_api_key or Config().get_str("CUZN_BRAZE_KEY")
        self.__timeout__ = timeout or Config().get_int("CUZN_BRAZE_TIMEOUT", 30)

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
