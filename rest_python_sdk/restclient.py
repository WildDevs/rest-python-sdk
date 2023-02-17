import typing as t

import requests

from .models.response import Response


class RESTClient:
    _base_url: str
    _timeout: int
    _headers: dict[str, t.Any]

    def __init__(self, base_url: str, timeout: int, headers: dict[str, t.Any]) -> None:
        self.base_url = base_url
        self.timeout = timeout
        self.headers = headers

    def __str__(self) -> str:
        return f"BaseURL: {self.base_url}\nTimeout: {self.timeout}"
        
    @property
    def base_url(self):
        return self._base_url
    
    @base_url.setter
    def base_url(self, value: str):
        if not value.startswith("https://"):
            print("Value is not a URL.")
            return
        else:
            self._base_url = value
    
    @property
    def timeout(self):
        return self._timeout
    
    @timeout.setter
    def timeout(self, value: int):
        if value > 30 or value < 5:
            print("Timeout must be a value between 5 and 30!")
        else:
            self._timeout = value
    
    @property
    def headers(self):
        return self._headers
    
    @headers.setter
    def headers(self, value: dict[str, t.Any]):
        self._headers = value


    def _request(self, method: str, endpoint: str, payload: t.Optional[dict[str, t.Any]] = None) -> Response:
        r = requests.request(method, f"{self.base_url}{endpoint}", headers=self.headers, json=payload)
        return Response(r.json())

    def get(self, endpoint: str):
        return self._request("GET", endpoint)

    def post(self, endpoint: str, payload: dict[str, t.Any]):
        return self._request("POST", endpoint, payload=payload)

    def put(self, endpoint: str, payload: dict[str, t.Any]):
        return self._request("PUT", endpoint, payload=payload)

    def delete(self, endpoint: str):
        return self._request("DELETE", endpoint)