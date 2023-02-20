from __future__ import annotations

__all__ = [
    "RESTClient",
]

import typing as t

import requests

from rest_python_sdk.models.response import APIResponse


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
        self, method: str, endpoint: str, payload: t.Optional[dict[str, t.Any]] = None
    ) -> APIResponse:
        r = requests.request(
            method, f"{self.base_url}{endpoint}", headers=self.headers, json=payload
        )
        return APIResponse(r.json(), r.headers)

    def get(self, endpoint: str):
        return self._request("GET", endpoint)

    def post(self, endpoint: str, payload: dict[str, t.Any]):
        return self._request("POST", endpoint, payload=payload)

    def put(self, endpoint: str, payload: dict[str, t.Any]):
        return self._request("PUT", endpoint, payload=payload)

    def delete(self, endpoint: str):
        return self._request("DELETE", endpoint)

    def validate_email(self, payload: dict[str, t.Any]):
        return self.post(f"{self.validate}email", payload=payload)

    def validate_btc(self, payload: dict[str, t.Any]):
        return self.post(f"{self.validate}btc", payload=payload)

    def validate_eth(self, payload: dict[str, t.Any]):
        return self.post(f"{self.validate}eth", payload=payload)

    def validate_bic(self, payload: dict[str, t.Any]):
        return self.post(f"{self.validate}bic", payload=payload)

    def validate_creditcard(self, payload: dict[str, t.Any]):
        return self.post(f"{self.validate}creditcard", payload=payload)

    def validate_ean(self, payload: dict[str, t.Any]):
        return self.post(f"{self.validate}ean", payload=payload)

    def validate_fqdn(self, payload: dict[str, t.Any]):
        return self.post(f"{self.validate}fqdn", payload=payload)

    def validate_iban(self, payload: dict[str, t.Any]):
        return self.post(f"{self.validate}iban", payload=payload)

    def validate_imei(self, payload: dict[str, t.Any]):
        return self.post(f"{self.validate}imei", payload=payload)

    def validate_ip(self, payload: dict[str, t.Any]):
        return self.post(f"{self.validate}ip", payload=payload)

    def validate_identitycard(self, payload: dict[str, t.Any]):
        return self.post(f"{self.validate}identitycard", payload=payload)

    def validate_isbn(self, payload: dict[str, t.Any]):
        return self.post(f"{self.validate}isbn", payload=payload)

    def validate_isin(self, payload: dict[str, t.Any]):
        return self.post(f"{self.validate}isin", payload=payload)

    def validate_issn(self, payload: dict[str, t.Any]):
        return self.post(f"{self.validate}issn", payload=payload)

    def validate_mac(self, payload: dict[str, t.Any]):
        return self.post(f"{self.validate}mac", payload=payload)

    def validate_magnet(self, payload: dict[str, t.Any]):
        return self.post(f"{self.validate}magnet", payload=payload)

    def validate_mimetype(self, payload: dict[str, t.Any]):
        return self.post(f"{self.validate}mimetype", payload=payload)

    def validate_password(self, payload: dict[str, t.Any]):
        return self.post(f"{self.validate}password", payload=payload)

    def validate_uuid(self, payload: dict[str, t.Any]):
        return self.post(f"{self.validate}uuid", payload=payload)

    def validate_tax(self, payload: dict[str, t.Any]):
        return self.post(f"{self.validate}tax", payload=payload)

    def validate_semver(self, payload: dict[str, t.Any]):
        return self.post(f"{self.validate}semver", payload=payload)

    def validate_licenseplate(self, payload: dict[str, t.Any]):
        return self.post(f"{self.validate}licenseplate", payload=payload)

    def validate_postalcode(self, payload: dict[str, t.Any]):
        return self.post(f"{self.validate}postalcode", payload=payload)

    # Utils Endpoint
    def utils_encode(self, payload: dict[str, t.Any]):
        return self.post(f"{self.utils}encode", payload=payload)

    def utils_decode(self, payload: dict[str, t.Any]):
        return self.post(f"{self.utils}decode", payload=payload)

    def utils_hash(self, payload: dict[str, t.Any]):
        return self.post(f"{self.utils}hash", payload=payload)

    # Random Endpoint
    def random_string(self, payload: dict[str, t.Any]):
        return self.post(f"{self.random}string", payload=payload)

    def random_number(self, payload: dict[str, t.Any]):
        return self.post(f"{self.random}number", payload=payload)
