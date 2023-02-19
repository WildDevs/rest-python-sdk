from __future__ import annotations

__all__ = [
    "WildDevsError",
    "BadRequestError",
    "send_error_response",
]

import typing as t


class WildDevsError(Exception):
    pass

class BadRequestError(WildDevsError):
    def __init__(self, error: str, *, not_allowed_fields: str | None = "", missing_fields: str | None = "") -> None:
        super().__init__(f"{error} {not_allowed_fields}{missing_fields}")

def send_error_response(data: dict[str, t.Any]):
    if data["code"] == 400:
        if "allowed" in data["note"]:
            raise BadRequestError(data["note"], not_allowed_fields=data["notAllowedFields"])
        if "missing" in data["note"]:
            raise BadRequestError(data["note"], missing_fields=data["missingFields"])
        raise BadRequestError(data["note"])
