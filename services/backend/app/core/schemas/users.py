from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    email: EmailStr = Field(...)
    type: int = Field(...)
    name: str = Field(...)
    surname: str = Field(...)
    midname: str = Field(...)
    birthday: date = Field(...)

class NewUser(User):
    password: str = Field(...)

class UserInDB(User):
    id: int = Field(...)
    hashed_password: str = Field(...)
