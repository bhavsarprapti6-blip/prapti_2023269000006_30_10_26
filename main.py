from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(title="Student Management API")

students_db: List = []

class Student(BaseModel):
    id: int
    name: str
    marks: float = Field(..., ge=0, le=100)

@app.post("/students", response_model=Student, status_code=201)
def add_student(student: Student):
    for existing in students_db:
        if existing.id == student.id:
            raise HTTPException(status_code=400, detail="Student already exists")
    students_db.append(student)
    return student

@app.get("/students", response_model=List[Student])
def get_students():
    return students_db

@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    for student in students_db:
        if student.id == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

# --- IMPROVED PUT ENDPOINT ---
@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students_db):
        if student.id == student_id:
            # Update data safely
            students_db[index] = updated_student
            return updated_student
    raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students_db):
        if student.id == student_id:
            students_db.pop(index)
            return {"message": "Student deleted successfully"}
    raise HTTPException(status_code=404, detail="Student not found")
