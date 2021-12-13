from datetime import date, datetime
from typing import Optional
from decimal import Decimal

from pydantic import BaseModel, Field

class Mark(BaseModel):
    student_id: int = Field(..., gt=0)
    work_id: int = Field(..., gt=0)
    mark: Decimal
    comment: Optional[str]

class MarkDB(Mark):
    id: int = Field(..., gt=0)
    creation_date: datetime = Field(...)
