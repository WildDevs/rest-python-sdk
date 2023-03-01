from __future__ import annotations

__all__ = [
    "RESTClient",
]

import typing as t
import base64

import requests
import aiohttp

from rest_python_sdk.models.response import APIResponse
from rest_python_sdk.errors.errors import send_error_response


class RESTClient:
    """
    The RestClient containing all endpoint methods. Implements sync and async variants.
    """

    _base_url: str
    _timeout: int
    _headers: dict[str, t.Any]
    _validate: str = "member/validate/"
    _utils: str = "public/utils/"
    _random: str = "public/random/"
    _compile: str = "member/compile/"
    _qrcode: str = "member/qrcode/"
    _geoip: str = "member/geoip/"
    _session: aiohttp.ClientSession

    def __init__(self, base_url: str, timeout: int, headers: dict[str, t.Any]) -> None:
        self.base_url = base_url
        self.timeout = timeout
        self.headers = headers

    def __str__(self) -> str:
        return f"BaseURL: {self.base_url}\nTimeout: {self.timeout}"

    @property
    def base_url(self):
        """The baseURL for all requests. Default is https://api.wild-devs.net/v1/."""
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
        """The amount of time to wait for a response, when a request has been made. Default is 30. Can be set between 5 and 30."""
        return self._timeout

    @timeout.setter
    def timeout(self, value: int):
        if value > 30 or value < 5:
            print("Timeout must be a value between 5 and 30!")
        else:
            self._timeout = value

    @property
    def headers(self):
        """The request headers of the API. More headers can be added manually."""
        return self._headers

    @headers.setter
    def headers(self, value: dict[str, t.Any]):
        self._headers = value

    @property
    def session(self):
        """The clientsession used for async requests. Has to be created using `create_session()`."""
        return self._session

    @session.setter
    def session(self, value: aiohttp.ClientSession):
        self._session = value

    def _build_payload(self, kwargs: dict[str, t.Any]) -> dict[str, t.Any]:
        """
        Helper method to create a payload from passed `**kwargs` if no payload has been supplied.

        Args:
            kwargs (`dict[str, t.Any]`): The `**kwargs` passed to an endpoint method.
        """
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

    def get(self, endpoint: str, return_headers: bool = False):
        """
        Synchronous GET request.

        Args:
            endpoint (`str`): The endpoint to send the request to.
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return self._request("GET", endpoint, return_headers=return_headers)

    def post(
        self,
        endpoint: str,
        payload: dict[str, t.Any],
        return_headers: bool = False,
    ):
        """
        Synchronous POST request.

        Args:
            endpoint (`str`): The endpoint to send the request to.
            payload (`dict`[`str`, `Any`]): The payload to send to the endpoint.
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return self._request("POST", endpoint, payload, return_headers=return_headers)

    def put(
        self,
        endpoint: str,
        payload: dict[str, t.Any],
        return_headers: bool = False,
    ):
        """
        Synchronous PUT request.

        Args:
            endpoint (`str`): The endpoint to send the request to.
            payload (`dict`[`str`, `Any`]): The payload to send to the endpoint.
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return self._request("PUT", endpoint, payload, return_headers=return_headers)

    def delete(self, endpoint: str, return_headers: bool = False):
        """
        Synchronous DELETE request.

        Args:
            endpoint (`str`): The endpoint to send the request to.
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return self._request("DELETE", endpoint, return_headers=return_headers)

    def validate_email(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/member/validate/email.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
                \temail (`str`): REQUIRED\n
                \tallow_display_name (`bool`): \n
                \trequire_display_name (`bool`):\n
                \tallow_utf8_local_part (`bool`):\n
                \tallow_ip_domain	(`bool`):\n
                \tdomain_specific_validation (`bool`):\n
                \tblacklisted_chrs (`str`): \n
                \thost_blacklist (`list`[`str`]):\n
                \thost_whitelist (`list`[`str`]):\n
                \tmx (`bool`):\n

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/member/validate/btc.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \taddress (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/member/validate/eth.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \taddress (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/member/validate/bic.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tbic (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/member/validate/creditcard.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tnumber (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/member/validate/ean.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tean (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/member/validate/fqdn.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tfqdn (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/member/validate/iban.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \taddress (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/member/validate/imei.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \timei (`str`): REQUIRED\n
            \tallow_hyphens (`bool`):

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/member/validate/ip.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tip (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/member/validate/identitycard.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tidentity (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/member/validate/isbn.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tisbn (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/member/validate/isin.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tisin (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/member/validate/issn.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tissn (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/member/validate/mac.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \taddress (`str`): REQUIRED\n
            \tno_separators (`bool`):

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/member/validate/magnet.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tmagnet (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/member/validate/mimetype.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tmimetype (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/member/validate/password.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tpassword (`str`): REQUIRED\n
            \tminLength	(`int`):\n
            \tminLowercase (`int`):\n
            \tminUppercase (`int`):\n
            \tminNumbers (`int`):\n
            \tminSymbols (`int`):\n
            \treturnScore (`bool`):\n
            \tpointsPerUnique	(`int`):\n
            \tpointsPerRepeat	(`int`):\n
            \tpointsForContainingLower	(`int`):\n
            \tpointsForContainingUpper	(`int`):\n
            \tpointsForContainingNumber	(`int`):\n
            \tpointsForContainingSymbol	(`int`):\n

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/member/validate/uuid.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tuuid (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/member/validate/tax.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \ttax (`str`): REQUIRED\n
            \tlocale (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/member/validate/semver.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tsemver (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/member/validate/licenseplate.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tlicenseplate (`str`): REQUIRED\n
            \tlocale (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/member/validate/postalcode.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tpostalcode (`str`): REQUIRED\n

        Returns:
            `APIResponse`: The object created from the response.
        """
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(
            f"{self._validate}postalcode", payload, return_headers=return_headers
        )

    def utils_encode(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/member/utils/encode.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/member/utils/decode.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/member/utils/hash.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(f"{self._utils}hash", payload, return_headers=return_headers)

    def random_string(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/public/random/string.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/public/random/number.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        if not payload:
            payload = self._build_payload(kwargs)
        return self.post(
            f"{self._random}number", payload, return_headers=return_headers
        )

    # Async HTTP methods

    def create_session(self):
        """
        Method to create a `ClientSession` for asynchronous requests.

        Returns:
            `ClientSession`: The client session needed to make asynchronous requests.
        """
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
        """
        Asynchronous GET request.

        Args:
            endpoint (`str`): The endpoint to send the request to.
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return await self._async_request("GET", endpoint, return_headers=return_headers)

    async def async_post(
        self,
        endpoint: str,
        payload: dict[str, t.Any],
        return_headers: bool = False,
    ):
        """
        Asynchronous POST request.

        Args:
            endpoint (`str`): The endpoint to send the request to.
            payload (`dict`[`str`, `Any`]): The payload to send to the endpoint.
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return await self._async_request(
            "POST", endpoint, payload, return_headers=return_headers
        )

    async def async_put(
        self,
        endpoint: str,
        payload: dict[str, t.Any],
        return_headers: bool = False,
    ):
        """
        Asynchronous PUT request.

        Args:
            endpoint (`str`): The endpoint to send the request to.
            payload (`dict`[`str`, `Any`]): The payload to send to the endpoint.
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return await self._async_request(
            "PUT", endpoint, payload, return_headers=return_headers
        )

    async def async_delete(self, endpoint: str, return_headers: bool = False):
        """
        Asynchronous DELETE request.

        Args:
            endpoint (`str`): The endpoint to send the request to.
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return await self._async_request(
            "DELETE", endpoint, return_headers=return_headers
        )

    async def async_validate_email(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/member/validate/email.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
                \temail (`str`): REQUIRED\n
                \tallow_display_name (`bool`): \n
                \trequire_display_name (`bool`):\n
                \tallow_utf8_local_part (`bool`):\n
                \tallow_ip_domain	(`bool`):\n
                \tdomain_specific_validation (`bool`):\n
                \tblacklisted_chrs (`str`): \n
                \thost_blacklist (`list`[`str`]):\n
                \thost_whitelist (`list`[`str`]):\n
                \tmx (`bool`):\n

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/member/validate/btc.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \taddress (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/member/validate/eth.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \taddress (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/member/validate/bic.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tbic (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/member/validate/creditcard.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tnumber (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/member/validate/ean.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tean (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/member/validate/fqdn.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tfqdn (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/member/validate/iban.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tiban (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/member/validate/imei.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \timei (`str`): REQUIRED\n
            \tallow_hyphens (`bool`): 

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/member/validate/ip.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tip (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/member/validate/identitycard.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tidentity (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/member/validate/isbn.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tisbn (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/member/validate/isin.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tisin (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/member/validate/issn.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tissn (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/member/validate/mac.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \taddress (`str`): REQUIRED\n
            \tno_separators (`str`): 

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/member/validate/magnet.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tmagnet (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/member/validate/mimetype.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tmimetype (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/member/validate/password.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tpassword (`str`): REQUIRED\n
            \tminLength	(`int`):\n
            \tminLowercase (`int`):\n
            \tminUppercase (`int`):\n
            \tminNumbers (`int`):\n
            \tminSymbols (`int`):\n
            \treturnScore (`bool`):\n
            \tpointsPerUnique	(`int`):\n
            \tpointsPerRepeat	(`int`):\n
            \tpointsForContainingLower	(`int`):\n
            \tpointsForContainingUpper	(`int`):\n
            \tpointsForContainingNumber	(`int`):\n
            \tpointsForContainingSymbol	(`int`):\n
        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/member/validate/uuid.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tuuid (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/member/validate/tax.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \ttax (`str`): REQUIRED\n
            \tlocale (`str`): REQUIRED
        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/member/validate/semver.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tsemver (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/member/validate/licenseplate.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tlicenseplate (`str`): REQUIRED\n
            \tlocale (`str`): REQUIRED

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/member/validate/postalcode.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.
            \tpostalcode (`str`): REQUIRED
            
        Returns:
            `APIResponse`: The object created from the response.
        """
        if not payload:
            payload = self._build_payload(kwargs)
        return await self.async_post(
            f"{self._validate}postalcode", payload, return_headers=return_headers
        )

    async def async_utils_encode(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/member/utils/encode.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/member/utils/decode.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/member/utils/hash.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/public/random/string.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/public/random/number.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/member/compile.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.

        Returns:
            `APIResponse`: The object created from the response.
        """
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
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/member/compile.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        if not payload:
            payload = self._build_payload(kwargs)
        return await self.async_post(
            f"{self._compile}", payload, return_headers=return_headers
        )

    def geoip(self, ip: str, *, return_headers: bool = False):
        """
        Method to send a synchronous GET request to https://api.wild-devs.net/v1/member/geoip/{ip}.

        Args:
            ip (`str`): The IPv4/IPv6 address to check.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return self.get(f"{self._geoip}{ip}", return_headers=return_headers)

    async def async_geoip(self, ip: str, *, return_headers: bool = False):
        """
        Method to send an asynchronous GET request to https://api.wild-devs.net/v1/member/geoip/{ip}.

        Args:
            ip (`str`): The IPv4/IPv6 address to check.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return await self.async_get(f"{self._geoip}{ip}", return_headers=return_headers)

    def qrcode(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        create_img: bool = False,
        file_path: str = "./",
        return_headers: bool = False,
        **kwargs: t.Any,
    ):
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/member/qrcode.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            create_img (`bool`): Decides if a .png will be created from the generated QR-code. Default is `False`.
            file_path (`str`): The filepath where the .png will be created. Default is the current directory.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        if not payload:
            payload = self._build_payload(kwargs)
        if not create_img:
            return self.post(f"{self._qrcode}", payload, return_headers=return_headers)
        else:
            data = self.post(f"{self._qrcode}", payload, return_headers=return_headers)
            code = data.data[21:]
            qr = base64.b64decode(code)
            with open(f"{file_path}qrcode.png", "wb") as f:
                f.write(qr)
            return data

    async def async_qrcode(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        create_img: bool = False,
        file_path: str = "./",
        **kwargs: t.Any,
    ):
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/member/qrcode.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            create_img (`bool`): Decides if a .png will be created from the generated QR-code. Default is `False`.
            file_path (`str`): The filepath where the .png will be created. Default is the current directory.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        if not payload:
            payload = self._build_payload(kwargs)
        if not create_img:
            return await self.async_post(
                f"{self._qrcode}", payload, return_headers=return_headers
            )
        else:
            data = await self.async_post(
                f"{self._qrcode}", payload, return_headers=return_headers
            )
            code = data.data[21:]
            qr = base64.b64decode(code)
            with open(f"{file_path}qrcode.png", "wb") as f:
                f.write(qr)
            return data
