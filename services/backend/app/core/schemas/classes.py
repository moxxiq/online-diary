from datetime import date
from typing import Optional

from pydantic import BaseModel, Field

class Class(BaseModel):
    name: str = Field(...)
    number: int = Field(...)

class ClassDB(Class):
    id: int = Field(..., gt=0)
