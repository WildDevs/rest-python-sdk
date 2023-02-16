import typing as t

import requests

from models.response import Response

class HTTPClient():
    _base_url: str
    _timeout: int
    _headers: dict[str, t.Any]

    def __init__(self, base_url: str, timeout: int, headers: dict[str, t.Any]) -> None:
        self.set_base_url(base_url)
        self.set_timeout(timeout)
        self.set_headers(headers)

    def __str__(self) -> str:
        return f"""
    BaseURL: {self.get_base_url()}
    Timeout: {self.get_timeout()}"""
        
    def get_base_url(self):
        return self._base_url


    def set_base_url(self, url: str):
        if not url.startswith("https://"):
            print("String is not a URL.")
            return
        else:
            self._base_url = url

    def get_timeout(self):
        return self._timeout

    def set_timeout(self, timeout: int):
        if timeout > 30 or timeout < 10:
            print("Timeout has to be between 10 and 30.")
            return
        else:
            self._timeout = timeout

    def get_headers(self):
        return self._headers

    def set_headers(self, headers: dict[str, t.Any]):
        self._headers = headers


    def get(self, endpoint: str):
        return Response(requests.get(f"{self.get_base_url()}{endpoint}", headers=self.get_headers()).json())

    def post(self, endpoint: str, payload: dict[str, t.Any]):
        return Response(requests.post(f"{self.get_base_url()}{endpoint}", json=payload, headers=self.get_headers()).json())

    def put(self, endpoint: str, payload: dict[str, t.Any]):
        return Response(requests.put(f"{self.get_base_url()}{endpoint}", json=payload, headers=self.get_headers()).json())

    def delete(self, endpoint: str):
        return Response(requests.delete(f"{self.get_base_url()}{endpoint}", self.get_headers()).json())