from datetime import date
from typing import Optional

from pydantic import BaseModel, Field

class WorkType(BaseModel):
    name: str = Field(...)

class WorkTypeDB(WorkType):
    id: int = Field(..., gt=0)
