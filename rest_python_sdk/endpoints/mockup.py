from __future__ import annotations

__all__ = [
    "Mockup",
]

import typing as t

from rest_python_sdk.restclient import RESTClient
from rest_python_sdk.models.response import APIResponse


class Mockup:
    """
    The endpoint class for mockup related endpoints.
    Contains sync and async variants of the endpoint methods.
    """

    _rest: RESTClient

    def __init__(self, rest: RESTClient) -> None:
        self._rest = rest

    @property
    def rest(self) -> RESTClient:
        return self._rest

    # Synchronous Methods

    def address(self, *, return_headers: bool = False) -> APIResponse:
        """
        Method to send a synchronous GET request to https://api.wild-devs.net/v1/address.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return self.rest.get(
            "address", return_headers=return_headers
        )

    def company(self, *, return_headers: bool = False) -> APIResponse:
        """
        Method to send a synchronous GET request to https://api.wild-devs.net/v1/company.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return self.rest.get(
            "company", return_headers=return_headers
        )

    def finance(self, *, return_headers: bool = False) -> APIResponse:
        """
        Method to send a synchronous GET request to https://api.wild-devs.net/v1/finance.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return self.rest.get(
            "finance", return_headers=return_headers
        )

    def git(self, *, return_headers: bool = False) -> APIResponse:
        """
        Method to send a synchronous GET request to https://api.wild-devs.net/v1/git.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return self.rest.get("git", return_headers=return_headers)

    def internet(self, *, return_headers: bool = False) -> APIResponse:
        """
        Method to send a synchronous GET request to https://api.wild-devs.net/v1/internet.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return self.rest.get(
            "internet", return_headers=return_headers
        )

    def product(self, *, return_headers: bool = False) -> APIResponse:
        """
        Method to send a synchronous GET request to https://api.wild-devs.net/v1/product.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return self.rest.get(
            "product", return_headers=return_headers
        )

    def user(self, *, return_headers: bool = False) -> APIResponse:
        """
        Method to send a synchronous GET request to https://api.wild-devs.net/v1/user.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return self.rest.get("user", return_headers=return_headers)

    def vehicle(self, *, return_headers: bool = False) -> APIResponse:
        """
        Method to send a synchronous GET request to https://api.wild-devs.net/v1/vehicle.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return self.rest.get(
            "vehicle", return_headers=return_headers
        )

    # Asynchronous Methods

    async def async_address(self, *, return_headers: bool = False) -> APIResponse:
        """
        Method to send an asynchronous GET request to https://api.wild-devs.net/v1/address.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return await self.rest.async_get(
            "address", return_headers=return_headers
        )

    async def async_company(self, *, return_headers: bool = False) -> APIResponse:
        """
        Method to send an asynchronous GET request to https://api.wild-devs.net/v1/company.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return await self.rest.async_get(
            "company", return_headers=return_headers
        )

    async def async_finance(self, *, return_headers: bool = False) -> APIResponse:
        """
        Method to send an asynchronous GET request to https://api.wild-devs.net/v1/finance.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return await self.rest.async_get(
            "finance", return_headers=return_headers
        )

    async def async_git(self, *, return_headers: bool = False) -> APIResponse:
        """
        Method to send an asynchronous GET request to https://api.wild-devs.net/v1/git.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return await self.rest.async_get(
            "git", return_headers=return_headers
        )

    async def async_internet(self, *, return_headers: bool = False) -> APIResponse:
        """
        Method to send an asynchronous GET request to https://api.wild-devs.net/v1/internet.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return await self.rest.async_get(
            "internet", return_headers=return_headers
        )

    async def async_product(self, *, return_headers: bool = False) -> APIResponse:
        """
        Method to send an asynchronous GET request to https://api.wild-devs.net/v1/product.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return await self.rest.async_get(
            "product", return_headers=return_headers
        )

    async def async_user(self, *, return_headers: bool = False) -> APIResponse:
        """
        Method to send an asynchronous GET request to https://api.wild-devs.net/v1/user.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return await self.rest.async_get(
            "user", return_headers=return_headers
        )

    async def async_vehicle(self, *, return_headers: bool = False) -> APIResponse:
        """
        Method to send an asynchronous GET request to https://api.wild-devs.net/v1/vehicle.

        Keyword Args:
            return_headers (`bool`): Decides if the `ResponseHeaders` should be included in the `APIResponse`. Default is `False`.

        Returns:
            `APIResponse`: The object created from the response.
        """
        return await self.rest.async_get(
            "vehicle", return_headers=return_headers
        )
