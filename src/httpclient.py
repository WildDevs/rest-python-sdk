import typing as t

import requests


class HTTPClient():
    base_url: str
    timeout: int

    def __init__(self, base_url: str, timeout: int) -> None:
        self.set_base_url(base_url)
        self.set_timeout(timeout)

    def __str__(self) -> str:
        return f"""
    BaseURL: {self.get_base_url()}
    Timeout: {self.get_timeout()}"""
        
    def get_base_url(self):
        return self.base_url

    def set_base_url(self, url: str):
        if not url.startswith("https://"):
            print("String is not a URL.")
            return
        else:
            self.base_url = url

    def get_timeout(self):
        return self.timeout

    def set_timeout(self, timeout: int):
        if timeout > 30 or timeout < 10:
            print("Timeout has to be between 10 and 30.")
            return
        else:
            self.timeout = timeout