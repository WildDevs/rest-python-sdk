import typing as t

from httpclient import HTTPClient

_endpoint: str = "public/utils/"

def encode(payload: dict[str, t.Any], httpclient: HTTPClient):
    return httpclient.post(f"{_endpoint}encode", payload=payload)

def decode(payload: dict[str, t.Any], httpclient: HTTPClient):
    return httpclient.post(f"{_endpoint}decode", payload=payload)

def hash(payload: dict[str, t.Any], httpclient: HTTPClient):
    return httpclient.post(f"{_endpoint}hash", payload=payload)