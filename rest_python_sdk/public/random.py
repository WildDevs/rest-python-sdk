from __future__ import annotations

__all__ = [
    "string",
    "number"
]

import typing as t

from rest_python_sdk.restclient import RESTClient

_endpoint: str = "public/random/"

def string(payload: dict[str, t.Any], rest: RESTClient):
    return rest.post(f"{_endpoint}string", payload=payload)

def number(payload: dict[str, t.Any], rest: RESTClient):
    return rest.post(f"{_endpoint}number", payload=payload)