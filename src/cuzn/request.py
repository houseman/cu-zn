from enum import Enum
from typing import Dict


class RequestMethod(Enum):
    GET = "GET"
    POST = "POST"


class BrazeRequest:
    def __init__(self, method: RequestMethod, path: str, data: Dict) -> None:
        self.__method__ = method
        self.__path__ = path
        self.__data__ = data
