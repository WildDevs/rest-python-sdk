import typing as t

from httpclient import HTTPClient

_endpoint: str = "public/random/"

def string(payload: dict[str, t.Any], httpclient: HTTPClient):
    return httpclient.post(f"{_endpoint}string", payload=payload)

def number(payload: dict[str, t.Any], httpclient: HTTPClient):
    return httpclient.post(f"{_endpoint}number", payload=payload)