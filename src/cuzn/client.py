import os
from typing import Optional

from .errors import ConfigurationError


class Client:
    _endpoint: Optional[str]
    _api_key: Optional[str]

    def __init__(
        self,
        *,
        braze_endpoint: Optional[str] = None,
        braze_api_key: Optional[str] = None
    ) -> None:
        self._endpoint = braze_endpoint or os.getenv("CUZN_BRAZE_ENDPOINT")
        self._api_key = braze_api_key or os.getenv("CUZN_BRAZE_API_KEY")

        if self._endpoint is None or self._api_key is None:
            raise ConfigurationError("Could not configure a Braze client")
