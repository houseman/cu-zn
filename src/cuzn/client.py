import os
from typing import Optional


class Client:
    _endpoint: Optional[str]
    _api_key: Optional[str]

    def __init__(
        self,
        *,
        braze_endpoint: Optional[str] = None,
        braze_api_key: Optional[str] = None
    ) -> None:
        self._endpoint = braze_endpoint or os.getenv("BRAZE_ENDPOINT")
        self._api_key = braze_api_key or os.getenv("BRAZE_API_KEY")

        if self._endpoint is None or self._api_key is None:
            raise Exception("Could not configure a Braze client")
