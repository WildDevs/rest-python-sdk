import base64
import typing as t

from httpclient import HTTPClient


class API():

    _x_api_key: str
    _headers: dict[str, t.Any]
    _httpclient: HTTPClient
    __version__ = "0.1.0"

    def __init__(self, *, 
    base_url: str | None = "https://api.wild-devs.net/v1/", 
    timeout: int | None = 30) -> None:
        self.set_headers({
            "User-Agent": f"Wild Devs API v{self.__version__} Python SDK",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.set_httpclient(HTTPClient(base_url, timeout, self.get_headers()))


    def __str__(self) -> str:
        return f"""
X-Api-Key: {self.get_x_api_key()}
Headers: {self.get_headers()}
HTTPClient: {self.get_httpclient()}
Version: {self.__version__}"""

    def get_x_api_key(self):
        return self._x_api_key

    def set_x_api_key(self, x_api_key: str) -> None:
        self._x_api_key = x_api_key

    def get_headers(self):
        return self._headers

    def set_headers(self, headers: dict[str, t.Any]):
        self._headers = headers

    def get_httpclient(self):
        return self._httpclient

    def set_httpclient(self, httpclient: HTTPClient):
        self._httpclient = httpclient

    def encode_api_key(self, key: str, secret: str):
        self.set_x_api_key(base64.b64encode(f"{key}:{secret}".encode("ascii")))
        self.get_headers()["x-api-key"] = self.get_x_api_key()
        self.get_httpclient().set_headers(self.get_headers())


api = API()

api.encode_api_key("WD-Z33623AQYLUFOYSZLFPQYAGVOJIY", "d-XW_9~Tz2BP.MKt7YF0HnnApO8aE8-kMUENa7l4")
