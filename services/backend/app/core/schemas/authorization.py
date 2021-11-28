from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, EmailStr


class Token(BaseModel):
    access_token: str = Field(...)
    token_type: str = Field(...)


class TokenData(BaseModel):
    username: str
    scopes: Optional[list[str]]

class TokenStatus(BaseModel):
    #  Sending status messages back to the end user
    message: str