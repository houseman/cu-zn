from typing import Dict, Optional

import ujson

from .request import BrazeRequest


class BrazeResponse:
    """API HTTP Response container class

    Properties are immutable, and values can ony be set at time of instantiation
    """

    __slots__ = ["__code__", "__content__", "__payload__", "__request__"]

    def __init__(self, code: int, content: str, request: BrazeRequest) -> None:
        """Constructor"""

        self.__code__ = code
        self.__content__ = content
        self.__payload__: Optional[Dict] = None
        self.__request__ = request

    @property
    def code(self) -> int:
        return self.__code__

    @property
    def content(self) -> str:
        return self.__content__

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}<{self.code}>"

    def is_success(self) -> bool:
        """Returns `True` if the API Response object has a status code of `2xx`"""

        return 200 <= self.code < 300

    def is_error(self) -> bool:
        """Returns `True` if the API Response object has a status code of `4xx`
        or `5xx`
        """

        return 400 <= self.code < 600

    @property
    def payload(self) -> Dict:
        """Return the response content payload as a JSON dictionary object"""

        # Use memoised result, if set
        if self.__payload__ is not None:
            return self.__payload__

        try:
            payload = ujson.loads(self.content)
        except (ujson.JSONDecodeError, TypeError):
            payload = {}

        self.__payload__ = payload

        return payload
