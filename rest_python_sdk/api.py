from __future__ import annotations

__all__ = [
    "WildDevsAPI",
]

import base64
import typing as t

from rest_python_sdk.restclient import RESTClient
from rest_python_sdk.__version__ import __version__


class WildDevsAPI():

    _x_api_key: str
    _headers: dict[str, t.Any]
    _rest: RESTClient

    def __init__(self, *, base_url: str | None = "https://api.wild-devs.net/v1/", timeout: int | None = 30) -> None:
        self.headers = {
            "User-Agent": f"Wild Devs API v{__version__} Python SDK",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        self.rest = RESTClient(base_url, timeout, self.headers)


    def __str__(self) -> str:
        return f"X-Api-Key: {self.x_api_key}\nHeaders: {self.headers}\nRESTClient: {self.rest}\nVersion: {self.__version__}"

    @property
    def x_api_key(self):
        return self._x_api_key
    
    @x_api_key.setter
    def x_api_key(self, value: str):
        self._x_api_key = value

    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, value: dict[str, t.Any]):
        self._headers = value

    @property
    def rest(self):
        return self._rest
    
    @rest.setter
    def rest(self, value: RESTClient):
        self._rest = value

    def encode_api_key(self, key: str, secret: str):
        self.x_api_key = base64.b64encode(f"{key}:{secret}".encode("ascii"))
        self.headers["x-api-key"] = self.x_api_key
        self.rest.headers = self.headers
