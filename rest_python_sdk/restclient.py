from __future__ import annotations

__all__ = [
    "RESTClient",
]

import typing as t

import requests

from rest_python_sdk.models.response import APIResponse
from rest_python_sdk.errors.errors import send_error_response


class RESTClient:
    _base_url: str
    _timeout: int
    _headers: dict[str, t.Any]
    _validate: str = "member/validate/"
    _utils: str = "public/utils/"
    _random: str = "public/random/"

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

    @property
    def validate(self):
        return self._validate

    @validate.setter
    def validate(self, value: str):
        self._validate = value

    @property
    def utils(self):
        return self._utils

    @utils.setter
    def utils(self, value: str):
        self._utils = value

    @property
    def random(self):
        return self._random

    @random.setter
    def random(self, value: str):
        self._random = value

    def _request(
        self,
        method: str,
        endpoint: str,
        payload: t.Optional[dict[str, t.Any]] = None,
        return_headers: t.Optional[bool] = False,
    ) -> APIResponse:
        r = requests.request(
            method, f"{self.base_url}{endpoint}", headers=self.headers, json=payload
        )
        if r.status_code == 404:
            resp = {
                "code": r.status_code,
                "note": f"{r.url} {r.reason}"
            }
            raise send_error_response(resp)
        if not return_headers:
            return APIResponse(r.json())
        else:
            return APIResponse(r.json(), r.headers)

    def get(self, endpoint: str, *, return_headers: t.Optional[bool] = False):
        return self._request("GET", endpoint, return_headers=return_headers)

    def post(
        self,
        endpoint: str,
        payload: dict[str, t.Any],
        return_headers: t.Optional[bool] = False,
    ):
        return self._request("POST", endpoint, payload, return_headers=return_headers)

    def put(
        self,
        endpoint: str,
        payload: dict[str, t.Any],
        return_headers: t.Optional[bool] = False,
    ):
        return self._request("PUT", endpoint, payload, return_headers)

    def delete(self, endpoint: str, return_headers: t.Optional[bool] = False):
        return self._request("DELETE", endpoint, return_headers)

    def validate_email(
        self, payload: dict[str, t.Any], *, return_headers: t.Optional[bool] = False
    ):
        return self.post(
            f"{self.validate}email", payload, return_headers=return_headers
        )

    def validate_btc(
        self, payload: dict[str, t.Any], *, return_headers: t.Optional[bool] = False
    ):
        return self.post(f"{self.validate}btc", payload, return_headers=return_headers)

    def validate_eth(
        self, payload: dict[str, t.Any], *, return_headers: t.Optional[bool] = False
    ):
        return self.post(f"{self.validate}eth", payload, return_headers=return_headers)

    def validate_bic(
        self, payload: dict[str, t.Any], *, return_headers: t.Optional[bool] = False
    ):
        return self.post(f"{self.validate}bic", payload, return_headers=return_headers)

    def validate_creditcard(
        self, payload: dict[str, t.Any], *, return_headers: t.Optional[bool] = False
    ):
        return self.post(
            f"{self.validate}creditcard", payload, return_headers=return_headers
        )

    def validate_ean(
        self, payload: dict[str, t.Any], *, return_headers: t.Optional[bool] = False
    ):
        return self.post(f"{self.validate}ean", payload, return_headers=return_headers)

    def validate_fqdn(
        self, payload: dict[str, t.Any], *, return_headers: t.Optional[bool] = False
    ):
        return self.post(f"{self.validate}fqdn", payload, return_headers=return_headers)

    def validate_iban(
        self, payload: dict[str, t.Any], *, return_headers: t.Optional[bool] = False
    ):
        return self.post(f"{self.validate}iban", payload, return_headers=return_headers)

    def validate_imei(
        self, payload: dict[str, t.Any], *, return_headers: t.Optional[bool] = False
    ):
        return self.post(f"{self.validate}imei", payload, return_headers=return_headers)

    def validate_ip(
        self, payload: dict[str, t.Any], *, return_headers: t.Optional[bool] = False
    ):
        return self.post(f"{self.validate}ip", payload, return_headers=return_headers)

    def validate_identitycard(
        self, payload: dict[str, t.Any], *, return_headers: t.Optional[bool] = False
    ):
        return self.post(
            f"{self.validate}identitycard", payload, return_headers=return_headers
        )

    def validate_isbn(
        self, payload: dict[str, t.Any], *, return_headers: t.Optional[bool] = False
    ):
        return self.post(f"{self.validate}isbn", payload, return_headers=return_headers)

    def validate_isin(
        self, payload: dict[str, t.Any], *, return_headers: t.Optional[bool] = False
    ):
        return self.post(f"{self.validate}isin", payload, return_headers=return_headers)

    def validate_issn(
        self, payload: dict[str, t.Any], *, return_headers: t.Optional[bool] = False
    ):
        return self.post(f"{self.validate}issn", payload, return_headers=return_headers)

    def validate_mac(
        self, payload: dict[str, t.Any], *, return_headers: t.Optional[bool] = False
    ):
        return self.post(f"{self.validate}mac", payload, return_headers=return_headers)

    def validate_magnet(
        self, payload: dict[str, t.Any], *, return_headers: t.Optional[bool] = False
    ):
        return self.post(
            f"{self.validate}magnet", payload, return_headers=return_headers
        )

    def validate_mimetype(
        self, payload: dict[str, t.Any], *, return_headers: t.Optional[bool] = False
    ):
        return self.post(
            f"{self.validate}mimetype", payload, return_headers=return_headers
        )

    def validate_password(
        self, payload: dict[str, t.Any], *, return_headers: t.Optional[bool] = False
    ):
        return self.post(
            f"{self.validate}password", payload, return_headers=return_headers
        )

    def validate_uuid(
        self, payload: dict[str, t.Any], *, return_headers: t.Optional[bool] = False
    ):
        return self.post(f"{self.validate}uuid", payload, return_headers=return_headers)

    def validate_tax(
        self, payload: dict[str, t.Any], *, return_headers: t.Optional[bool] = False
    ):
        return self.post(f"{self.validate}tax", payload, return_headers=return_headers)

    def validate_semver(
        self, payload: dict[str, t.Any], *, return_headers: t.Optional[bool] = False
    ):
        return self.post(
            f"{self.validate}semver", payload, return_headers=return_headers
        )

    def validate_licenseplate(
        self, payload: dict[str, t.Any], *, return_headers: t.Optional[bool] = False
    ):
        return self.post(
            f"{self.validate}licenseplate", payload, return_headers=return_headers
        )

    def validate_postalcode(
        self, payload: dict[str, t.Any], *, return_headers: t.Optional[bool] = False
    ):
        return self.post(
            f"{self.validate}postalcode", payload, return_headers=return_headers
        )

    # Utils Endpoint
    def utils_encode(
        self, payload: dict[str, t.Any], *, return_headers: t.Optional[bool] = False
    ):
        return self.post(f"{self.utils}encode", payload, return_headers=return_headers)

    def utils_decode(
        self, payload: dict[str, t.Any], *, return_headers: t.Optional[bool] = False
    ):
        return self.post(f"{self.utils}decode", payload, return_headers=return_headers)

    def utils_hash(
        self, payload: dict[str, t.Any], *, return_headers: t.Optional[bool] = False
    ):
        return self.post(f"{self.utils}hash", payload, return_headers=return_headers)

    # Random Endpoint
    def random_string(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        method: str = "",
        length: int = 30,
        min: int = 30,
        max: int = 30,
        pool: str = "",
        prefix: str = "",
        batch: int = 0,
        dashes: bool = True,
        name: str = "",
        namespace: str = "",
        return_headers: t.Optional[bool] = False,
    ):
        if not payload:
            payload = {
                "method": method,
                "length": length,
                "min": min,
                "max": max,
                "pool": pool,
                "prefix": prefix,
                "batch": batch,
                "dashes": dashes,
                "name": name,
                "namespace": namespace
            }
        return self.post(f"{self.random}string", payload, return_headers=return_headers)

    def random_number(
        self, payload: dict[str, t.Any], *, return_headers: t.Optional[bool] = False
    ):
        return self.post(f"{self.random}number", payload, return_headers=return_headers)
