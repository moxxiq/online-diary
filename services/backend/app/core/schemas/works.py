from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, Field

class WorkContent(BaseModel):
    headline: str = Field(...)
    deadline: Optional[datetime]
    description: Optional[str]
    work_type_id: int = Field(..., gt=0)

class Work(WorkContent):
    workplace_id: int = Field(..., gt=0)

class WorkDB(Work):
    id: int = Field(..., gt=0)
    creation_date: datetime = Field(...)
