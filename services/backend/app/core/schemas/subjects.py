from pydantic import BaseModel, Field

class Subject(BaseModel):
    name: str = Field(...)

class SubjectDB(Subject):
    id: int = Field(..., gt=0)
