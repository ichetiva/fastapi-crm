from typing import Optional

from pydantic import BaseModel


class LoginResponseScheme(BaseModel):
    status: str
    message: str


class LoginRequestScheme(BaseModel):
    email: str


class ConfirmLoginResponseScheme(BaseModel):
    status: str
    message: Optional[str] = None
    token: Optional[str] = None
