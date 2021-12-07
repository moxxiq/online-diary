from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, Field

class Work(BaseModel):
    workplace_id: int = Field(..., gt=0)
    worktype_id: int = Field(..., gt=0)
    headline: str = Field(...)
    deadline: Optional[datetime]
    description: Optional[str]

class WorkDB(Work):
    id: int = Field(..., gt=0)
    creation_date: datetime = Field(...)
