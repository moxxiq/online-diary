from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel, Field

class Class(BaseModel):
    name: str = Field(...)
    number: int = datetime.now().year

class ClassDB(Class):
    id: int = Field(..., gt=0)
