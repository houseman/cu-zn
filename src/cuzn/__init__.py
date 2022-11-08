from typing import Optional

from .client import Client


def configure(
    braze_endpoint: Optional[str] = None, braze_api_key: Optional[str] = None
) -> Client:
    """
    Return a configured Braze Client instance
    """

    return Client(braze_endpoint=braze_endpoint, braze_api_key=braze_api_key)
