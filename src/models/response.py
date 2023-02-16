import typing as t
from dataclasses import dataclass

@dataclass
class Response():

    _status: str
    _code: int
    _message: str
    _note: str
    _data: t.Any

    def __init__(self, data: dict[str, t.Any]) -> None:
        self.set_status(data["status"])
        self.set_code(data["code"])
        self.set_message(data["message"])
        self.set_data(data["data"])
        
        if data["note"]:
            self.set_note(data["note"])
        
    def __str__(self) -> str:
        return f"""
Status: {self.get_status()}
Code: {self.get_code()}
Message: {self.get_message()}
Note: {self.get_note()}
Data: {self.get_data()}"""

    def get_status(self):
        return self._status
    
    def set_status(self, status: str):
        self._status = status
    
    def get_code(self):
        return self._code

    def set_code(self, code: int):
        self._code = code
    
    def get_message(self):
        return self._message
    
    def set_message(self, message: str):
        self._message = message
    
    def get_data(self):
        return self._data
    
    def set_data(self, data: t.Any):
        self._data = data
    
    def get_note(self):
        return self._note

    def set_note(self, note: str):
        self._note = note