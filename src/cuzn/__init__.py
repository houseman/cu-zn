from typing import Optional

from .client import BrazeClient


def configure(
    braze_endpoint: Optional[str] = None, braze_api_key: Optional[str] = None
) -> BrazeClient:
    """
    Return a configured Braze BrazeClient instance
    """

    return BrazeClient(braze_endpoint=braze_endpoint, braze_api_key=braze_api_key)
