from datetime import date
import enum

from pydantic import BaseModel, Field, EmailStr

class UserType(enum.Enum):
    administration = 1
    teacher = 2
    student = 3

class UserSchema(BaseModel):
    id: int = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    type: UserType = Field(...)
    name: str = Field(...)
    surname: str = Field(...)
    midname: str = Field(...)
    birthday: date = Field(...)

class UserInDB(UserSchema):
    hashed_password: str