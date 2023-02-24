from __future__ import annotations

__all__ = [
    "ResponseHeaders",
]

from datetime import datetime
import typing as t


class ResponseHeaders:
    _server: str
    _date: datetime
    _content_type: str
    _content_length: int
    _connection: str
    _x_powered_by: str
    _access_control_allow_origin: str
    _access_control_allow_headers: str
    _x_ratelimit_retry_after: float
    _x_ratelimit_limit: int
    _x_ratelimit_remaining: int
    _x_ratelimit_reset: datetime
    _etag: str
    _vary: str
    _strict_transport_security: str
    _referrer_policy: str
    _x_content_type_options: str
    _x_download_options: str
    _x_frame_options: str
    _x_permitted_cross_domain_policies: str
    _x_robots_tag: str
    _x_xss_protection: str
    _as_dict: t.Union[t.MutableMapping[str, t.Any], t.Mapping[str, t.Any]]

    def __init__(
        self, headers: t.Union[t.MutableMapping[str, t.Any], t.Mapping[str, t.Any]]
    ) -> None:
        self._server = headers["Server"]
        self._date = datetime.strptime(headers["Date"], "%a, %d %b %Y %H:%M:%S %Z")
        self._content_type = headers["Content-Type"]
        self._content_length = int(headers["Content-Length"])
        self._connection = headers["Connection"]
        self._x_powered_by = headers["X-Powered-By"]
        self._access_control_allow_origin = headers["Access-Control-Allow-Origin"]
        self._access_control_allow_headers = headers["Access-Control-Allow-Headers"]
        self._x_ratelimit_retry_after = float(headers["x-ratelimit-retry-after"])
        self._x_ratelimit_limit = int(headers["x-ratelimit-limit"])
        self._x_ratelimit_remaining = int(headers["x-ratelimit-remaining"])
        self._x_ratelimit_reset = datetime.strptime(
            headers["x-ratelimit-reset"], "%a %b %d %Y %H:%M:%S %Z%z"
        )
        self._etag = headers["ETag"]
        self._vary = headers["Vary"]
        self._strict_transport_security = headers["Strict-Transport-Security"]
        self._referrer_policy = headers["Referrer-Policy"]
        self._x_content_type_options = headers["X-Content-Type-Options"]
        self._x_download_options = headers["X-Download-Options"]
        self._x_frame_options = headers["X-Frame-Options"]
        self._x_permitted_cross_domain_policies = headers[
            "X-Permitted-Cross-Domain-Policies"
        ]
        self._x_robots_tag = headers["X-Robots-Tag"]
        self._x_xss_protection = headers["X-XSS-Protection"]
        self._as_dict = headers

    def __str__(self) -> str:
        return f"{self.as_dict}"

    @property
    def server(self):
        return self._server

    @property
    def date(self):
        return self._date

    @property
    def content_type(self):
        return self._content_type

    @property
    def content_length(self):
        return self._content_length

    @property
    def connection(self):
        return self._connection

    @property
    def x_powered_by(self):
        return self._x_powered_by

    @property
    def access_control_allow_origin(self):
        return self._access_control_allow_origin

    @property
    def access_control_allow_headers(self):
        return self._access_control_allow_headers

    @property
    def x_ratelimit_retry_after(self):
        return self._x_ratelimit_retry_after

    @property
    def x_ratelimit_limit(self):
        return self._x_ratelimit_limit

    @property
    def x_ratelimit_remaining(self):
        return self._x_ratelimit_remaining

    @property
    def x_ratelimit_reset(self):
        return self._x_ratelimit_reset

    @property
    def etag(self):
        return self._etag

    @property
    def vary(self):
        return self._vary

    @property
    def strict_transport_security(self):
        return self._strict_transport_security

    @property
    def referrer_policy(self):
        return self._referrer_policy

    @property
    def x_content_type_options(self):
        return self._x_content_type_options

    @property
    def x_download_options(self):
        return self._x_download_options

    @property
    def x_frame_options(self):
        return self._x_frame_options

    @property
    def x_permitted_cross_domain_policies(self):
        return self._x_permitted_cross_domain_policies

    @property
    def x_robots_tag(self):
        return self._x_robots_tag

    @property
    def x_xss_protection(self):
        return self._x_xss_protection

    @property
    def as_dict(self):
        return self._as_dict
