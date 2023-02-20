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
    code = data["code"]
    error = data["note"]
    if code == 400:
        if not_allowed_fields := data.get("notAllowedFields"):
            return BadRequestError(
                error, not_allowed_fields=not_allowed_fields
            )
        if missing_fields :=  data.get("missingFields"):
            return BadRequestError(error, missing_fields=missing_fields)
        return BadRequestError(error)
    return error_dict[code](error)


error_dict: dict[int, type[WildDevsError]] = {
    401: UnauthorizedError,
    403: ForbiddenError,
    404: NotFoundError,
    500: InternalServerError,
    502: BadGatewayError,
    503: ServiceUnavailableError,
    504: GatewayTimeoutError
}