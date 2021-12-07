from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, Field

class Mark(BaseModel):
    student_id: int = Field(..., gt=0)
    work_id: int = Field(..., gt=0)
    comment: Optional[str]

class MarkDB(Mark):
    id: int = Field(..., gt=0)
    creation_date: datetime = Field(...)
