from __future__ import annotations

__all__ = [
    "Random",
]

import typing as t

from wild_devs_api.restclient import RESTClient
from wild_devs_api.models.response import APIResponse


class Random:
    """
    The endpoint class for random related endpoints.
    Contains sync and async variants of the endpoint methods.
    """

    _rest: RESTClient

    def __init__(self, rest: RESTClient) -> None:
        self._rest = rest

    @property
    def rest(self) -> RESTClient:
        return self._rest

    # Synchronous Methods

    def string(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        xml: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/string.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        if not payload:
            payload = self.rest._build_payload(kwargs)
        return self.rest.post("string", payload, return_headers=return_headers, xml=xml)

    def number(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        xml: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/number.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        if not payload:
            payload = self.rest._build_payload(kwargs)
        return self.rest.post("number", payload, return_headers=return_headers, xml=xml)

    def joke(self, *, return_headers: bool = False, xml: bool = False) -> APIResponse:
        """
        Method to send a synchronous GET request to https://api.wild-devs.net/v1/joke.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return self.rest.get("joke", return_headers=return_headers, xml=xml)

    # Asynchronous Methods

    async def async_string(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/string.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        if not payload:
            payload = self.rest._build_payload(kwargs)
        return await self.rest.async_post(
            "string", payload, return_headers=return_headers
        )

    async def async_number(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/number.

        Args:
            payload (Optional`dict`[`str`, `Any`]): The payload to send to the endpoint.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.
            **kwargs (`Any`): The additional kwargs that have to be passed if payload is `None`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        if not payload:
            payload = self.rest._build_payload(kwargs)
        return await self.rest.async_post(
            "number", payload, return_headers=return_headers
        )

    async def async_joke(self, *, return_headers: bool = False) -> APIResponse:
        """
        Method to send an asynchronous GET request to https://api.wild-devs.net/v1/joke.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return await self.rest.async_get("joke", return_headers=return_headers)
