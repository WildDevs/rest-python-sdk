from __future__ import annotations

__all__ = [
    "email",
    "btc",
    "eth",
    "bic",
    "creditcard",
    "ean",
    "fqdn",
    "iban",
    "imei",
    "ip",
    "identitycard",
    "isbn",
    "isin",
    "issn",
    "mac",
    "magnet",
    "mimetype",
    "password",
    "uuid",
    "tax",
    "semver",
    "licenseplate",
    "postalcode"
]

import typing as t

from rest_python_sdk.restclient import RESTClient

_endpoint: str = "member/validate/"

def email(payload: dict[str, t.Any], RESTClient: RESTClient):
    return RESTClient.post(f"{_endpoint}email", payload=payload)

def btc(payload: dict[str, t.Any], RESTClient: RESTClient):
    return RESTClient.post(f"{_endpoint}btc", payload=payload)

def eth(payload: dict[str, t.Any], RESTClient: RESTClient):
    return RESTClient.post(f"{_endpoint}eth", payload=payload)

def bic(payload: dict[str, t.Any], RESTClient: RESTClient):
    return RESTClient.post(f"{_endpoint}bic", payload=payload)

def creditcard(payload: dict[str, t.Any], RESTClient: RESTClient):
    return RESTClient.post(f"{_endpoint}creditcard", payload=payload)

def ean(payload: dict[str, t.Any], RESTClient: RESTClient):
    return RESTClient.post(f"{_endpoint}ean", payload=payload)

def fqdn(payload: dict[str, t.Any], RESTClient: RESTClient):
    return RESTClient.post(f"{_endpoint}fqdn", payload=payload)

def iban(payload: dict[str, t.Any], RESTClient: RESTClient):
    return RESTClient.post(f"{_endpoint}iban", payload=payload)

def imei(payload: dict[str, t.Any], RESTClient: RESTClient):
    return RESTClient.post(f"{_endpoint}imei", payload=payload)

def ip(payload: dict[str, t.Any], RESTClient: RESTClient):
    return RESTClient.post(f"{_endpoint}ip", payload=payload)

def identitycard(payload: dict[str, t.Any], RESTClient: RESTClient):
    return RESTClient.post(f"{_endpoint}identitycard", payload=payload)

def isbn(payload: dict[str, t.Any], RESTClient: RESTClient):
    return RESTClient.post(f"{_endpoint}isbn", payload=payload)

def isin(payload: dict[str, t.Any], RESTClient: RESTClient):
    return RESTClient.post(f"{_endpoint}isin", payload=payload)

def issn(payload: dict[str, t.Any], RESTClient: RESTClient):
    return RESTClient.post(f"{_endpoint}issn", payload=payload)

def mac(payload: dict[str, t.Any], RESTClient: RESTClient):
    return RESTClient.post(f"{_endpoint}mac", payload=payload)

def magnet(payload: dict[str, t.Any], RESTClient: RESTClient):
    return RESTClient.post(f"{_endpoint}magnet", payload=payload)

def mimetype(payload: dict[str, t.Any], RESTClient: RESTClient):
    return RESTClient.post(f"{_endpoint}mimetype", payload=payload)

def password(payload: dict[str, t.Any], RESTClient: RESTClient):
    return RESTClient.post(f"{_endpoint}password", payload=payload)

def uuid(payload: dict[str, t.Any], RESTClient: RESTClient):
    return RESTClient.post(f"{_endpoint}uuid", payload=payload)

def tax(payload: dict[str, t.Any], RESTClient: RESTClient):
    return RESTClient.post(f"{_endpoint}tax", payload=payload)

def semver(payload: dict[str, t.Any], RESTClient: RESTClient):
    return RESTClient.post(f"{_endpoint}semver", payload=payload)

def licenseplate(payload: dict[str, t.Any], RESTClient: RESTClient):
    return RESTClient.post(f"{_endpoint}licenseplate", payload=payload)

def postalcode(payload: dict[str, t.Any], RESTClient: RESTClient):
    return RESTClient.post(f"{_endpoint}postalcode", payload=payload)