from datetime import date
from typing import Optional

from pydantic import BaseModel, Field

class Student(BaseModel):
    user_id: int = Field(..., gt=0)
    class_id: int = Field(..., gt=0)
