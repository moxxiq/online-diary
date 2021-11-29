from datetime import date
import enum

from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)
    type: int = Field(...)
    name: str = Field(...)
    surname: str = Field(...)
    midname: str = Field(...)
    birthday: date = Field(...)

class UserInDB(User):
    id: int = Field(...)
    hashed_password: str = Field(...)