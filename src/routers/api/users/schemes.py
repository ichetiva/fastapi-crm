from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class UserResponseScheme(BaseModel):
    email: str
    first_name: str
    last_name: Optional[str] = None
    created_at: datetime
    last_login_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class CreateUserRequestScheme(BaseModel):
    email: str
    first_name: str
    last_name: Optional[str] = None


class UpdateUserRequestScheme(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
