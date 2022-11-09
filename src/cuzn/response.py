from typing import Dict, Optional

import ujson


class ApiResponse:
    """API HTTP Response container class

    Properties are immutable, and values can ony be set at time of instantiation
    """

    __slots__ = ["_code", "_content", "_payload"]

    def __init__(self, code: int, content: str) -> None:
        """Constructor"""

        self._code = code
        self._content = content
        self._payload: Optional[Dict] = None

    @property
    def code(self) -> int:
        return self._code

    @property
    def content(self) -> str:
        return self._content

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

    def payload(self) -> Dict:
        """Return the response content payload as a JSON dictionary object"""

        # USe memoised result, if set
        if self._payload is not None:
            return self._payload

        try:
            payload = ujson.loads(self.content)
        except (ujson.JSONDecodeError, TypeError):
            payload = {}

        self._payload = payload

        return payload
