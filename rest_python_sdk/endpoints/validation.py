from __future__ import annotations

__all__ = [
    "Validation",
]

import typing as t

from rest_python_sdk.restclient import RESTClient
from rest_python_sdk.models.response import APIResponse


class Validation:
    """
    The endpoint class for validation related endpoints.
    Contains sync and async variants of the endpoint methods.
    """

    _rest: RESTClient

    def __init__(self, rest: RESTClient) -> None:
        self._rest = rest

    @property
    def rest(self) -> RESTClient:
        return self._rest

    # Synchronous Methods

    def email(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/email.

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
            payload = self.rest._build_payload(kwargs)
        return self.rest.post(
            f"{self.rest.base_url}email", payload, return_headers=return_headers
        )

    def btc(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/btc.

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
            payload = self.rest._build_payload(kwargs)
        return self.rest.post(
            f"{self.rest.base_url}btc", payload, return_headers=return_headers
        )

    def eth(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/eth.

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
            payload = self.rest._build_payload(kwargs)
        return self.rest.post(
            f"{self.rest.base_url}eth", payload, return_headers=return_headers
        )

    def bic(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/bic.

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
            payload = self.rest._build_payload(kwargs)
        return self.rest.post(
            f"{self.rest.base_url}bic", payload, return_headers=return_headers
        )

    def creditcard(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/creditcard.

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
            payload = self.rest._build_payload(kwargs)
        return self.rest.post(
            f"{self.rest.base_url}creditcard",
            payload,
            return_headers=return_headers,
        )

    def ean(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/ean.

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
            payload = self.rest._build_payload(kwargs)
        return self.rest.post(
            f"{self.rest.base_url}ean", payload, return_headers=return_headers
        )

    def fqdn(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/fqdn.

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
            payload = self.rest._build_payload(kwargs)
        return self.rest.post(
            f"{self.rest.base_url}fqdn", payload, return_headers=return_headers
        )

    def iban(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/iban.

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
            payload = self.rest._build_payload(kwargs)
        return self.rest.post(
            f"{self.rest.base_url}iban", payload, return_headers=return_headers
        )

    def imei(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/imei.

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
            payload = self.rest._build_payload(kwargs)
        return self.rest.post(
            f"{self.rest.base_url}imei", payload, return_headers=return_headers
        )

    def ip(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/ip.

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
            payload = self.rest._build_payload(kwargs)
        return self.rest.post(
            f"{self.rest.base_url}ip", payload, return_headers=return_headers
        )

    def identitycard(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/identitycard.

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
            payload = self.rest._build_payload(kwargs)
        return self.rest.post(
            f"{self.rest.base_url}identitycard",
            payload,
            return_headers=return_headers,
        )

    def isbn(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/isbn.

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
            payload = self.rest._build_payload(kwargs)
        return self.rest.post(
            f"{self.rest.base_url}isbn", payload, return_headers=return_headers
        )

    def isin(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/isin.

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
            payload = self.rest._build_payload(kwargs)
        return self.rest.post(
            f"{self.rest.base_url}isin", payload, return_headers=return_headers
        )

    def issn(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/issn.

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
            payload = self.rest._build_payload(kwargs)
        return self.rest.post(
            f"{self.rest.base_url}issn", payload, return_headers=return_headers
        )

    def mac(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/mac.

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
            payload = self.rest._build_payload(kwargs)
        return self.rest.post(
            f"{self.rest.base_url}mac", payload, return_headers=return_headers
        )

    def magnet(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/magnet.

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
            payload = self.rest._build_payload(kwargs)
        return self.rest.post(
            f"{self.rest.base_url}magnet", payload, return_headers=return_headers
        )

    def mimetype(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/mimetype.

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
            payload = self.rest._build_payload(kwargs)
        return self.rest.post(
            f"{self.rest.base_url}mimetype", payload, return_headers=return_headers
        )

    def password(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/password.

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
            payload = self.rest._build_payload(kwargs)
        return self.rest.post(
            f"{self.rest.base_url}password", payload, return_headers=return_headers
        )

    def uuid(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/uuid.

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
            payload = self.rest._build_payload(kwargs)
        return self.rest.post(
            f"{self.rest.base_url}uuid", payload, return_headers=return_headers
        )

    def tax(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/tax.

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
            payload = self.rest._build_payload(kwargs)
        return self.rest.post(
            f"{self.rest.base_url}tax", payload, return_headers=return_headers
        )

    def semver(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/semver.

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
            payload = self.rest._build_payload(kwargs)
        return self.rest.post(
            f"{self.rest.base_url}semver", payload, return_headers=return_headers
        )

    def licenseplate(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/licenseplate.

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
            payload = self.rest._build_payload(kwargs)
        return self.rest.post(
            f"{self.rest.base_url}licenseplate",
            payload,
            return_headers=return_headers,
        )

    def postalcode(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/postalcode.

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
            payload = self.rest._build_payload(kwargs)
        return self.rest.post(
            f"{self.rest.base_url}postalcode",
            payload,
            return_headers=return_headers,
        )

    # Asynchronous Methods

    async def async_email(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/email.

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
            payload = self.rest._build_payload(kwargs)
        return await self.rest.async_post(
            f"{self.rest.base_url}email", payload, return_headers=return_headers
        )

    async def async_btc(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/btc.

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
            payload = self.rest._build_payload(kwargs)
        return await self.rest.async_post(
            f"{self.rest.base_url}btc", payload, return_headers=return_headers
        )

    async def async_eth(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/eth.

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
            payload = self.rest._build_payload(kwargs)
        return await self.rest.async_post(
            f"{self.rest.base_url}eth", payload, return_headers=return_headers
        )

    async def async_bic(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/bic.

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
            payload = self.rest._build_payload(kwargs)
        return await self.rest.async_post(
            f"{self.rest.base_url}bic", payload, return_headers=return_headers
        )

    async def async_creditcard(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/creditcard.

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
            payload = self.rest._build_payload(kwargs)
        return await self.rest.async_post(
            f"{self.rest.base_url}creditcard",
            payload,
            return_headers=return_headers,
        )

    async def async_ean(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/ean.

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
            payload = self.rest._build_payload(kwargs)
        return await self.rest.async_post(
            f"{self.rest.base_url}ean", payload, return_headers=return_headers
        )

    async def async_fqdn(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/fqdn.

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
            payload = self.rest._build_payload(kwargs)
        return await self.rest.async_post(
            f"{self.rest.base_url}fqdn", payload, return_headers=return_headers
        )

    async def async_iban(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/iban.

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
            payload = self.rest._build_payload(kwargs)
        return await self.rest.async_post(
            f"{self.rest.base_url}iban", payload, return_headers=return_headers
        )

    async def async_imei(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/imei.

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
            payload = self.rest._build_payload(kwargs)
        return await self.rest.async_post(
            f"{self.rest.base_url}imei", payload, return_headers=return_headers
        )

    async def async_ip(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/ip.

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
            payload = self.rest._build_payload(kwargs)
        return await self.rest.async_post(
            f"{self.rest.base_url}ip", payload, return_headers=return_headers
        )

    async def async_identitycard(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/identitycard.

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
            payload = self.rest._build_payload(kwargs)
        return await self.rest.async_post(
            f"{self.rest.base_url}identitycard",
            payload,
            return_headers=return_headers,
        )

    async def async_isbn(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/isbn.

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
            payload = self.rest._build_payload(kwargs)
        return await self.rest.async_post(
            f"{self.rest.base_url}isbn", payload, return_headers=return_headers
        )

    async def async_isin(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/isin.

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
            payload = self.rest._build_payload(kwargs)
        return await self.rest.async_post(
            f"{self.rest.base_url}isin", payload, return_headers=return_headers
        )

    async def async_issn(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/issn.

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
            payload = self.rest._build_payload(kwargs)
        return await self.rest.async_post(
            f"{self.rest.base_url}issn", payload, return_headers=return_headers
        )

    async def async_mac(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/mac.

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
            payload = self.rest._build_payload(kwargs)
        return await self.rest.async_post(
            f"{self.rest.base_url}mac", payload, return_headers=return_headers
        )

    async def async_magnet(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/magnet.

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
            payload = self.rest._build_payload(kwargs)
        return await self.rest.async_post(
            f"{self.rest.base_url}magnet", payload, return_headers=return_headers
        )

    async def async_mimetype(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/mimetype.

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
            payload = self.rest._build_payload(kwargs)
        return await self.rest.async_post(
            f"{self.rest.base_url}mimetype", payload, return_headers=return_headers
        )

    async def async_password(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/password.

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
            payload = self.rest._build_payload(kwargs)
        return await self.rest.async_post(
            f"{self.rest.base_url}password", payload, return_headers=return_headers
        )

    async def async_uuid(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/uuid.

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
            payload = self.rest._build_payload(kwargs)
        return await self.rest.async_post(
            f"{self.rest.base_url}uuid", payload, return_headers=return_headers
        )

    async def async_tax(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/tax.

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
            payload = self.rest._build_payload(kwargs)
        return await self.rest.async_post(
            f"{self.rest.base_url}tax", payload, return_headers=return_headers
        )

    async def async_semver(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/semver.

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
            payload = self.rest._build_payload(kwargs)
        return await self.rest.async_post(
            f"{self.rest.base_url}semver", payload, return_headers=return_headers
        )

    async def async_licenseplate(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/licenseplate.

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
            payload = self.rest._build_payload(kwargs)
        return await self.rest.async_post(
            f"{self.rest.base_url}licenseplate",
            payload,
            return_headers=return_headers,
        )

    async def async_postalcode(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/postalcode.

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
            payload = self.rest._build_payload(kwargs)
        return await self.rest.async_post(
            f"{self.rest.base_url}postalcode",
            payload,
            return_headers=return_headers,
        )
