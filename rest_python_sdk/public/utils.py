from __future__ import annotations

__all__ = ["encode", "decode", "hash"]

import typing as t

from rest_python_sdk.restclient import RESTClient

_endpoint: str = "public/utils/"


def encode(payload: dict[str, t.Any], rest: RESTClient):
    return rest.post(f"{_endpoint}encode", payload=payload)


def decode(payload: dict[str, t.Any], rest: RESTClient):
    return rest.post(f"{_endpoint}decode", payload=payload)


def hash(payload: dict[str, t.Any], rest: RESTClient):
    return rest.post(f"{_endpoint}hash", payload=payload)
