from pydantic import BaseModel, Field
from typing import Optional

class StudentCreate(BaseModel):
    name: str = Field(..., example="Rahul Sharma")
    age: int = Field(..., gt=0, example=20)
    course: str = Field(..., example="MSc IT")
    city: str = Field(..., example="Ahmedabad")

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    course: Optional[str] = None
    city: Optional[str] = None

class StudentResponse(StudentCreate):
    id: int