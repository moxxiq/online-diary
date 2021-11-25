from datetime import date

from pydantic import BaseModel, Field, EmailStr


class Token(BaseModel):
    access_token: str = Field(...)
    token_type: str = Field(...)


class TokenData(BaseModel):
    email: EmailStr
    scopes: list[str] | None

class TokenStatus(BaseModel):
    #  Sending status messages back to the end user
    message: str