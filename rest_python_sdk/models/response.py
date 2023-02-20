from __future__ import annotations

__all__ = [
    "APIResponse",
]

import typing as t
from dataclasses import dataclass

from rest_python_sdk.errors.errors import send_error_response
from rest_python_sdk.models.response_headers import ResponseHeaders


@dataclass
class APIResponse:
    _status: str
    _code: int
    _message: str
    _data: t.Any
    _headers: ResponseHeaders

    def __init__(self, data: dict[str, t.Any], headers: dict[str, str]) -> None:
        if data["code"] >= 400:
            raise send_error_response(data)
        self.status = data["status"]
        self.code = data["code"]
        self.message = data["message"]
        self.data = data["data"]
        self.headers = ResponseHeaders(headers)

    def __str__(self) -> str:
        return f"Status: {self.status}\nCode: {self.code}\nMessage: {self.message}\nData: {self.data}"

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value: str):
        self._status = value

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value: int):
        self._code = value

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value: str):
        self._message = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, value):
        self._headers = value
