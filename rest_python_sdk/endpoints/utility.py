from __future__ import annotations

__all__ = [
    "Utility",
]

import typing as t
import base64

from rest_python_sdk.restclient import RESTClient
from rest_python_sdk.models.response import APIResponse


class Utility:
    """
    The endpoint class for utility related endpoints.
    Contains sync and async variants of the endpoint methods.
    """

    _rest: RESTClient

    def __init__(self, rest: RESTClient) -> None:
        self._rest = rest

    @property
    def rest(self) -> RESTClient:
        return self._rest

    # Synchronous Methods

    def compile(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/compile.

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
        return self.rest.post(
            "compile", payload, return_headers=return_headers
        )

    def decode(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/decode.

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
        return self.rest.post(
            "decode", payload, return_headers=return_headers
        )

    def encode(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/encode.

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
        return self.rest.post(
            "encode", payload, return_headers=return_headers
        )

    def hash(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/hash.

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
        return self.rest.post(
            "hash", payload, return_headers=return_headers
        )

    def qrcode(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        create_img: bool = False,
        file_path: str = "./",
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send a synchronous POST request to https://api.wild-devs.net/v1/qrcode.

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
            payload = self.rest._build_payload(kwargs)
        if not create_img:
            return self.rest.post(
                "qrcode", payload, return_headers=return_headers
            )
        else:
            data = self.rest.post(
                "qrcode", payload, return_headers=return_headers
            )
            code = data.data[21:]
            qr = base64.b64decode(code)
            with open(f"{file_path}qrcode.png", "wb") as f:
                f.write(qr)
            return data

    # Asynchronous Methods

    async def async_compile(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/compile.

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
            "compile", payload, return_headers=return_headers
        )

    async def async_decode(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/decode.

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
            "decode", payload, return_headers=return_headers
        )

    async def async_encode(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/encode.

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
            "encode", payload, return_headers=return_headers
        )

    async def async_hash(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/hash.

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
            "hash", payload, return_headers=return_headers
        )

    async def async_qrcode(
        self,
        payload: t.Optional[dict[str, t.Any]] = None,
        *,
        create_img: bool = False,
        file_path: str = "./",
        return_headers: bool = False,
        **kwargs: t.Any,
    ) -> APIResponse:
        """
        Method to send an asynchronous POST request to https://api.wild-devs.net/v1/qrcode.

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
            payload = self.rest._build_payload(kwargs)
        if not create_img:
            return await self.rest.async_post(
                "qrcode", payload, return_headers=return_headers
            )
        else:
            data = await self.rest.async_post(
                "qrcode", payload, return_headers=return_headers
            )
            code = data.data[21:]
            qr = base64.b64decode(code)
            async with open(f"{file_path}qrcode.png", "wb") as f:
                f.write(qr)
            return data
