from __future__ import annotations

__all__ = [
    "NetTools",
]

import typing as t

from rest_python_sdk.restclient import RESTClient
from rest_python_sdk.models.response import APIResponse

class NetTools:
    """
    The endpoint class for net tools related endpoints.
    Contains sync and async variants of the endpoint methods.
    """

    _rest: RESTClient

    def __init__(self, rest: RESTClient) -> None:
        self._rest = rest

    @property
    def rest(self) -> RESTClient:
        return self._rest

    # Synchronous Methods

    def dnslookup(self, source: str, *, return_headers: bool = False) -> APIResponse:
        """
        Method to send a synchronous GET request to https://api.wild-devs.net/v1/dnslookup.

        Args:
            source (`str`): The FQDN (Full Qualified Domain Name).

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return self.rest.get(
            f"dnslookup?{source}", return_headers=return_headers
        )

    def ipinfo(self, ip: str, *, return_headers: bool = False) -> APIResponse:
        """
        Method to send a synchronous GET request to https://api.wild-devs.net/v1/ipinfo.

        Args:
            ip (`str`): The IPv4/IPv6 address to check.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return self.rest.get(
            f"ipinfo?{ip}", return_headers=return_headers
        )

    def geoip(self, ip: str, *, return_headers: bool = False) -> APIResponse:
        """
        Method to send a synchronous GET request to https://api.wild-devs.net/v1/geoip/{ip}.

        Args:
            ip (`str`): The IPv4/IPv6 address to check.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return self.rest.get(
            f"geoip/{ip}", return_headers=return_headers
        )

    def whatsmyip(self, *, return_headers: bool = False) -> APIResponse:
        """
        Method to send a synchronous GET request to https://api.wild-devs.net/v1/whatsmyip.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return self.rest.get(
            "whatsmyip", return_headers=return_headers
        )

    # Asynchronous Methods

    async def async_dnslookup(
        self, source: str, *, return_headers: bool = False
    ) -> APIResponse:
        """
        Method to send an asynchronous GET request to https://api.wild-devs.net/v1/dnslookup.

        Args:
            source (`str`): The FQDN (Full Qualified Domain Name).

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return await self.rest.async_get(
            f"dnslookup?{source}", return_headers=return_headers
        )

    async def async_ipinfo(
        self, ip: str, *, return_headers: bool = False
    ) -> APIResponse:
        """
        Method to send an asynchronous GET request to https://api.wild-devs.net/v1/ipinfo.

        Args:
            ip (`str`): The IPv4/IPv6 address to check.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return await self.rest.async_get(
            f"ipinfo?{ip}", return_headers=return_headers
        )

    async def async_geoip(
        self, ip: str, *, return_headers: bool = False
    ) -> APIResponse:
        """
        Method to send an asynchronous GET request to https://api.wild-devs.net/v1/geoip/{ip}.

        Args:
            ip (`str`): The IPv4/IPv6 address to check.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return await self.rest.async_get(
            f"geoip/{ip}", return_headers=return_headers
        )

    async def async_whatsmyip(
        self, *, return_headers: bool = False
    ) -> APIResponse:
        """
        Method to send an asynchronous GET request to https://api.wild-devs.net/v1/whatsmyip.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return await self.rest.async_get(
            "whatsmyip", return_headers=return_headers
        )