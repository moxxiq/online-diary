from datetime import date, datetime
from typing import Optional
from decimal import Decimal

from pydantic import BaseModel, Field

class MarkContent(BaseModel):
    mark: Decimal
    comment: Optional[str]

class Mark(MarkContent):
    student_id: int = Field(..., gt=0)
    work_id: int = Field(..., gt=0)

class MarkDB(Mark):
    id: int = Field(..., gt=0)
    creation_date: datetime = Field(...)
