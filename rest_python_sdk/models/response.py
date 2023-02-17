from __future__ import annotations

__all__ = [
    "Response",
]

import typing as t
from dataclasses import dataclass


@dataclass
class Response:
    _status: str
    _code: int
    _message: str
    _note: str
    _data: t.Any

    def __init__(self, data: dict[str, t.Any]) -> None:
        self.status = data["status"]
        self.code = data["code"]
        self.message = data["message"]
        self.data = data["data"]

        if "note" in data.keys():
            self.note = data["note"]
        else:
            self.note = ""

    def __str__(self) -> str:
        return f"Status: {self.status}\nCode: {self.code}\nMessage: {self.message}\nNote: {self.note}\nData: {self.data}"

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
    def note(self):
        return self._note

    @note.setter
    def note(self, value: str):
        self._note = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
