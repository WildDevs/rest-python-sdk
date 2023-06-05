from __future__ import annotations

__all__ = [
    "OpenData",
]

import typing as t

from wild_devs_api.restclient import RESTClient
from wild_devs_api.models.response import APIResponse


class OpenData:
    """
    The endpoint class for open data related endpoints.
    Contains sync and async variants of the endpoint methods.
    """

    _rest: RESTClient

    def __init__(self, rest: RESTClient) -> None:
        self._rest = rest

    @property
    def rest(self) -> RESTClient:
        return self._rest

    # Synchronous Methods

    def domains(
        self,
        *,
        return_headers: bool = False,
        xml: bool = False,
    ) -> APIResponse:
        """
        Method to send a synchronous GET request to https://api.wild-devs.net/v1/domains.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return self.rest.get("domains", return_headers=return_headers, xml=xml)

    # Asynchronous Methods

    async def async_domains(
        self,
        *,
        return_headers: bool = False,
    ) -> APIResponse:
        """
        Method to send an asynchronous GET request to https://api.wild-devs.net/v1/domains.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return await self.rest.async_get("domains", return_headers=return_headers)
