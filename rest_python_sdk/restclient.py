from __future__ import annotations

__all__ = [
    "RESTClient",
]

import typing as t

import requests
import aiohttp

from rest_python_sdk.models.response import APIResponse
from rest_python_sdk.errors.errors import send_error_response


class RESTClient:
    _base_url: str
    _timeout: int
    _headers: dict[str, t.Any]
    _validate: str = "member/validate/"
    _utils: str = "public/utils/"
    _random: str = "public/random/"
    _compile: str = "member/compile/"
    _session: aiohttp.ClientSession

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
    def session(self):
        return self._session

    @session.setter
    def session(self, value: aiohttp.ClientSession):
        self._session = value

    def _build_payload(self, kwargs: dict[str, t.Any]) -> dict[str, t.Any]:
        payload: dict[str, t.Any] = {}
        for k in kwargs:
            payload[k] = kwargs[k]
        return payload

    # Sync Base Requests
    def _request(
        self,
        method: str,
        endpoint: str,
        payload: t.Optional[dict[str, t.Any]] = None,
        return_headers: bool = False,
    ) -> APIResponse:
        r = requests.request(
            method, f"{self.base_url}{endpoint}", headers=self.headers, json=payload
        )
        if r.status_code == 404:
            resp = {"code": r.status_code, "note": f"{r.url} {r.reason}"}
            raise send_error_response(resp)
        if not return_headers:
            return APIResponse(r.json())
        else:
            return APIResponse(r.json(), r.headers)

    def get(self, endpoint: str, *, return_headers: bool = False):
        return self._request("GET", endpoint, return_headers=return_headers)

    def post(
        self,
        endpoint: str,
        payload: dict[str, t.Any],
        return_headers: bool = False,
    ):
        return self._request("POST", endpoint, payload, return_headers=return_headers)

    def put(
        self,
        endpoint: str,
        payload: dict[str, t.Any],
        return_headers: bool = False,
    ):
        return self._request("PUT", endpoint, payload, return_headers=return_headers)

    def delete(self, endpoint: str, return_headers: bool = False):
        return self._request("DELETE", endpoint, return_headers=return_headers)

    # Validate Endpoint
    def validate_email(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(
            f"{self._validate}email", payload, return_headers=return_headers
        )

    def validate_btc(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(f"{self._validate}btc", payload, return_headers=return_headers)

    def validate_eth(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(f"{self._validate}eth", payload, return_headers=return_headers)

    def validate_bic(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(f"{self._validate}bic", payload, return_headers=return_headers)

    def validate_creditcard(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(
            f"{self._validate}creditcard", payload, return_headers=return_headers
        )

    def validate_ean(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(f"{self._validate}ean", payload, return_headers=return_headers)

    def validate_fqdn(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(
            f"{self._validate}fqdn", payload, return_headers=return_headers
        )

    def validate_iban(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(
            f"{self._validate}iban", payload, return_headers=return_headers
        )

    def validate_imei(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(
            f"{self._validate}imei", payload, return_headers=return_headers
        )

    def validate_ip(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(f"{self._validate}ip", payload, return_headers=return_headers)

    def validate_identitycard(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(
            f"{self._validate}identitycard", payload, return_headers=return_headers
        )

    def validate_isbn(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(
            f"{self._validate}isbn", payload, return_headers=return_headers
        )

    def validate_isin(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(
            f"{self._validate}isin", payload, return_headers=return_headers
        )

    def validate_issn(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(
            f"{self._validate}issn", payload, return_headers=return_headers
        )

    def validate_mac(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(f"{self._validate}mac", payload, return_headers=return_headers)

    def validate_magnet(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(
            f"{self._validate}magnet", payload, return_headers=return_headers
        )

    def validate_mimetype(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(
            f"{self._validate}mimetype", payload, return_headers=return_headers
        )

    def validate_password(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(
            f"{self._validate}password", payload, return_headers=return_headers
        )

    def validate_uuid(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(
            f"{self._validate}uuid", payload, return_headers=return_headers
        )

    def validate_tax(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(f"{self._validate}tax", payload, return_headers=return_headers)

    def validate_semver(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(
            f"{self._validate}semver", payload, return_headers=return_headers
        )

    def validate_licenseplate(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(
            f"{self._validate}licenseplate", payload, return_headers=return_headers
        )

    def validate_postalcode(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(
            f"{self._validate}postalcode", payload, return_headers=return_headers
        )

    # _utils Endpoint
    def utils_encode(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(f"{self._utils}encode", payload, return_headers=return_headers)

    def utils_decode(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(f"{self._utils}decode", payload, return_headers=return_headers)

    def utils_hash(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(f"{self._utils}hash", payload, return_headers=return_headers)

    # Random Endpoint
    def random_string(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(
            f"{self._random}string", payload, return_headers=return_headers
        )

    def random_number(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(
            f"{self._random}number", payload, return_headers=return_headers
        )

    # Async HTTP methods

    def create_session(self):
        self.session = aiohttp.ClientSession(headers=self.headers)

    async def _async_request(
        self,
        method: str,
        endpoint: str,
        payload: t.Optional[dict[str, t.Any]] = None,
        return_headers: bool = False,
    ):
        async with self.session.request(
            method, f"{self.base_url}{endpoint}", json=payload
        ) as r:
            if r.status == 404:
                resp = {"code": r.status, "note": f"{r.url} {r.reason}"}
                raise send_error_response(resp)
            if not return_headers:
                return APIResponse(await r.json())
            else:
                return APIResponse(await r.json(), r.headers)

    async def async_get(self, endpoint: str, *, return_headers: bool = False):
        return await self._async_request("GET", endpoint, return_headers=return_headers)

    async def async_post(
        self,
        endpoint: str,
        payload: dict[str, t.Any],
        return_headers: bool = False,
    ):
        return await self._async_request(
            "POST", endpoint, payload, return_headers=return_headers
        )

    async def async_put(
        self,
        endpoint: str,
        payload: dict[str, t.Any],
        return_headers: bool = False,
    ):
        return await self._async_request(
            "PUT", endpoint, payload, return_headers=return_headers
        )

    async def async_delete(self, endpoint: str, return_headers: bool = False):
        return await self._async_request(
            "DELETE", endpoint, return_headers=return_headers
        )

    # Validate Endpoint
    async def async_validate_email(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return await self.async_post(
            f"{self._validate}email", payload, return_headers=return_headers
        )

    async def async_validate_btc(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return await self.async_post(
            f"{self._validate}btc", payload, return_headers=return_headers
        )

    async def async_validate_eth(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return await self.async_post(
            f"{self._validate}eth", payload, return_headers=return_headers
        )

    async def async_validate_bic(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return await self.async_post(
            f"{self._validate}bic", payload, return_headers=return_headers
        )

    async def async_validate_creditcard(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return await self.async_post(
            f"{self._validate}creditcard", payload, return_headers=return_headers
        )

    async def async_validate_ean(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return await self.async_post(
            f"{self._validate}ean", payload, return_headers=return_headers
        )

    async def async_validate_fqdn(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return await self.async_post(
            f"{self._validate}fqdn", payload, return_headers=return_headers
        )

    async def async_validate_iban(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return await self.async_post(
            f"{self._validate}iban", payload, return_headers=return_headers
        )

    async def async_validate_imei(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return await self.async_post(
            f"{self._validate}imei", payload, return_headers=return_headers
        )

    async def async_validate_ip(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return await self.async_post(
            f"{self._validate}ip", payload, return_headers=return_headers
        )

    async def async_validate_identitycard(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return await self.async_post(
            f"{self._validate}identitycard", payload, return_headers=return_headers
        )

    async def async_validate_isbn(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return await self.async_post(
            f"{self._validate}isbn", payload, return_headers=return_headers
        )

    async def async_validate_isin(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return await self.async_post(
            f"{self._validate}isin", payload, return_headers=return_headers
        )

    async def async_validate_issn(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return await self.async_post(
            f"{self._validate}issn", payload, return_headers=return_headers
        )

    async def async_validate_mac(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return await self.async_post(
            f"{self._validate}mac", payload, return_headers=return_headers
        )

    async def async_validate_magnet(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return await self.async_post(
            f"{self._validate}magnet", payload, return_headers=return_headers
        )

    async def async_validate_mimetype(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return await self.async_post(
            f"{self._validate}mimetype", payload, return_headers=return_headers
        )

    async def async_validate_password(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return await self.async_post(
            f"{self._validate}password", payload, return_headers=return_headers
        )

    async def async_validate_uuid(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return await self.async_post(
            f"{self._validate}uuid", payload, return_headers=return_headers
        )

    async def async_validate_tax(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return await self.async_post(
            f"{self._validate}tax", payload, return_headers=return_headers
        )

    async def async_validate_semver(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return await self.async_post(
            f"{self._validate}semver", payload, return_headers=return_headers
        )

    async def async_validate_licenseplate(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return await self.async_post(
            f"{self._validate}licenseplate", payload, return_headers=return_headers
        )

    async def async_validate_postalcode(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return await self.async_post(
            f"{self._validate}postalcode", payload, return_headers=return_headers
        )

    # Async Utils Endpoint
    async def async_utils_encode(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return await self.async_post(
            f"{self._utils}encode", payload, return_headers=return_headers
        )

    async def async_utils_decode(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return await self.async_post(
            f"{self._utils}decode", payload, return_headers=return_headers
        )

    async def async_utils_hash(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return await self.async_post(
            f"{self._utils}hash", payload, return_headers=return_headers
        )

    # Async Random Endpoint
    async def async_random_string(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return await self.async_post(
            f"{self._random}string", payload, return_headers=return_headers
        )

    async def async_random_number(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return await self.async_post(
            f"{self._random}number", payload, return_headers=return_headers
        )

    # Compile Endpoint
    def compile(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(f"{self._compile}", payload, return_headers=return_headers)

    async def async_compile(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        if not payload:
            payload = self._build_payload(kwargs)
        return await self.async_post(
            f"{self._compile}", payload, return_headers=return_headers
        )
