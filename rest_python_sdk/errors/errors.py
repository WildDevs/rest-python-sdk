from __future__ import annotations

__all__ = [
    "WildDevsError",
    "BadRequestError",
    "send_error_response",
    "UnauthorizedError",
    "ForbiddenError",
    "NotFoundError",
    "InternalServerError",
    "BadGatewayError",
    "ServiceUnavailableError",
    "GatewayTimeoutError",
]

import typing as t


class WildDevsError(Exception):
    pass


class BadRequestError(WildDevsError):
    def __init__(
        self,
        error: str,
        *,
        not_allowed_fields: str | None = "",
        missing_fields: str | None = "",
    ) -> None:
        super().__init__(f"{error} {not_allowed_fields}{missing_fields}")


class UnauthorizedError(WildDevsError):
    def __init__(self, error: str) -> None:
        super().__init__(error)


class ForbiddenError(WildDevsError):
    def __init__(self, error: str) -> None:
        super().__init__(error)


class NotFoundError(WildDevsError):
    def __init__(self, error: str) -> None:
        super().__init__(error)


class InternalServerError(WildDevsError):
    def __init__(self, error: str) -> None:
        super().__init__(error)


class BadGatewayError(WildDevsError):
    def __init__(self, error: str) -> None:
        super().__init__(error)


class ServiceUnavailableError(WildDevsError):
    def __init__(self, error: str) -> None:
        super().__init__(error)


class GatewayTimeoutError(WildDevsError):
    def __init__(self, error: str) -> None:
        super().__init__(error)


def send_error_response(data: dict[str, t.Any]):
    if data["code"] == 400:
        if "allowed" in data["note"]:
            return BadRequestError(
                data["note"], not_allowed_fields=data["notAllowedFields"]
            )
        if "missing" in data["note"]:
            return BadRequestError(data["note"], missing_fields=data["missingFields"])
        return BadRequestError(data["note"])
    if data["code"] == 401:
        return UnauthorizedError(data["note"])
    if data["code"] == 403:
        return ForbiddenError(data["note"])
    if data["code"] == 404:
        return NotFoundError(data["note"])
    if data["code"] == 500:
        return InternalServerError(data["note"])
    if data["code"] == 502:
        return BadGatewayError(data["note"])
    if data["code"] == 503:
        return ServiceUnavailableError(data["note"])
    if data["code"] == 504:
        return GatewayTimeoutError(data["note"])
