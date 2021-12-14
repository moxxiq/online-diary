from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    email: EmailStr = Field(...)
    type: int = Field(...)
    name: str = Field(...)
    surname: str = Field(...)
    midname: Optional[str]
    birthday: Optional[date]

class NewUser(User):
    password: str = Field(...)

class UserWithID(User):
    id: int = Field(...)

class UserInDB(UserWithID):
    hashed_password: str = Field(...)
