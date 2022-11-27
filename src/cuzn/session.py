import requests

from .request import BrazeRequest
from .response import BrazeResponse


class BrazeSession:
    def __init__(self, *, session: requests.Session) -> None:
        self.__session__ = session

    def send(self, request: BrazeRequest) -> BrazeResponse:
        __request__ = requests.Request(
            method=request.__method__, url=request.__path__, data=request.__data__
        )
        prepared_request = __request__.prepare()
        response = self.__session__.send(request=prepared_request)

        return BrazeResponse(
            code=response.status_code, content=response.text, request=request
        )
