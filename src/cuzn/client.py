import os
from typing import Optional, TypeVar

import requests
from dotenv import load_dotenv

from .errors import ConfigurationError

Self = TypeVar("Self", bound="BrazeClient")


class BrazeClient:
    _endpoint: Optional[str]
    _api_key: Optional[str]

    def __init__(
        self,
        *,
        braze_endpoint: Optional[str] = None,
        braze_api_key: Optional[str] = None,
    ) -> None:
        load_dotenv()  # load environment variables from .env file

        self._endpoint = braze_endpoint or os.getenv("CUZN_BRAZE_ENDPOINT")
        self._api_key = braze_api_key or os.getenv("CUZN_BRAZE_API_KEY")

        self._validate_config()

    def create(self: Self) -> Self:
        """
        Create the configured client session
        """

        self._validate_config()

        self._session = requests.Session()
        self._session.headers.update(
            {
                "Authorization": f"Bearer {self._api_key}",
                "Content-Type": "application/json",
            }
        )

        return self

    def _validate_config(self) -> None:
        """
        Validate the instance configuration. Raises a `ConfigurationError` exception if
        the validation fails.
        """

        try:
            assert self._endpoint is not None
            assert self._api_key is not None
        except AssertionError:
            raise ConfigurationError("Could not configure a Braze client")
