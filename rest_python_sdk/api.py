from __future__ import annotations

__all__ = [
    "WildDevsAPI",
]

import base64
import typing as t

import aiohttp

from rest_python_sdk.restclient import RESTClient
from rest_python_sdk.endpoints.conversion import Conversion
from rest_python_sdk.endpoints.games import Games
from rest_python_sdk.endpoints.mockup import Mockup
from rest_python_sdk.endpoints.random import Random
from rest_python_sdk.endpoints.urlshortener import UrlShortener
from rest_python_sdk.endpoints.utility import Utility
from rest_python_sdk.endpoints.validation import Validation
from rest_python_sdk.__version__ import __version__


class WildDevsAPI:
    """
    Base class of the WildDevsAPI wrapper.
    Includes a `RESTClient` and `AsyncRESTClient` with all endpoint methods.
    """

    _x_api_key: str
    _headers: dict[str, t.Any]
    _rest: RESTClient
    _session: aiohttp.ClientSession
    _conversion: Conversion
    _games: Games
    _mockup: Mockup
    _random: Random
    _urlshortener: UrlShortener
    _utility: Utility
    _validation: Validation

    def __init__(
        self,
        *,
        base_url: str = "https://api.wild-devs.net/v1/",
        timeout: int = 30,
    ) -> None:
        self._headers = {
            "User-Agent": f"Wild Devs API v{__version__} Python SDK",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        self._rest = RESTClient(base_url, timeout, self._headers)
        self._conversion = Conversion(self._rest)
        self._games = Games(self._rest)
        self._mockup = Mockup(self._rest)
        self._random = Random(self._rest)
        self._urlshortener = UrlShortener(self._rest)
        self._utility = Utility(self._rest)
        self._validation = Validation(self._rest)

    def __str__(self) -> str:
        return f"X-Api-Key: {self.x_api_key}\nHeaders: {self.headers}\nRESTClient: {self.rest}\nVersion: {__version__}"

    @property
    def x_api_key(self) -> str:
        """The api-key used for member/subscriber endpoint requests."""
        return self._x_api_key

    @property
    def headers(self) -> dict[str, t.Any]:
        """The request headers of the API. More headers can be added manually."""
        return self._headers

    @property
    def rest(self) -> RESTClient:
        """The `RESTClient` of the API. Contains raw HTTP requests."""
        return self._rest

    @property
    def session(self) -> aiohttp.ClientSession:
        """The `ClientSession` used for async requests. Has to be created using `create_session()`."""
        return self._session

    @property
    def conversion(self) -> Conversion:
        """The class containing conversion related endpoint methods."""
        return self._conversion

    @property
    def games(self) -> Games:
        """The class containing game related endpoint methods."""
        return self._games

    @property
    def mockup(self) -> Mockup:
        """The class containing mockup related endpoint methods."""
        return self._mockup

    @property
    def random(self) -> Random:
        """The class containing random related endpoint methods."""
        return self._random

    @property
    def urlshortener(self) -> UrlShortener:
        """The class containing urlshortener related endpoint methods."""
        return self._urlshortener

    @property
    def validation(self) -> Validation:
        """The class containing validation related endpoint methods."""
        return self._validation

    def encode_api_key(self, key: str, secret: str) -> None:
        """
        Method to turn the api-key and secret into base64 and add it to the headers. This is required to be able to use the member/subscriber endpoints.

        Args:
            key (`str`): The API key generated on https://wild-devs.net/account/keys. Always starts with `WD-`.
            secret (`str`): The secret generated besides the API key.
        """
        self._x_api_key = base64.b64encode(f"{key}:{secret}".encode("utf-8")).decode(
            "utf-8"
        )
        self._headers["x-api-key"] = self.x_api_key
        self._rest.headers = self.headers
        self._conversion = Conversion(self._rest)
        self._games = Games(self._rest)
        self._mockup = Mockup(self._rest)
        self._random = Random(self._rest)
        self._urlshortener = UrlShortener(self._rest)
        self._utility = Utility(self._rest)
        self._validation = Validation(self._rest)

    def create_session(self) -> None:
        """
        Method to create a `ClientSession` for asynchronous requests.

        Returns:
            `ClientSession`: The client session needed to make asynchronous requests.
        """
        self._session = aiohttp.ClientSession(headers=self.headers)
