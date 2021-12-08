from datetime import date
from typing import Optional

from pydantic import BaseModel, Field

class Teacher(BaseModel):
    user_id: int = Field(..., gt=0)
    position: str = Field(...)
