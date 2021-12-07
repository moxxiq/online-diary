from datetime import date
from typing import Optional

from pydantic import BaseModel, Field

class Workplace(BaseModel):
    class_id: int = Field(...)
    subject_id: int = Field(...)
    teacher_id: int = Field(...)

class WorkplaceDB(Workplace):
    id: int = Field(..., gt=0)
