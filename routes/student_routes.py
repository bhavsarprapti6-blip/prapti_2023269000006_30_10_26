from fastapi import APIRouter, Query, status
from typing import List, Optional
from models.student import StudentCreate, StudentUpdate, StudentResponse
from controllers import student_controller

router = APIRouter(prefix="/students", tags=["Students CRUD"])

@router.get("/", response_model=List[StudentResponse], status_code=status.HTTP_200_OK)
def read_students(search: Optional[str] = Query(None, description="Search by name or course")):
    return student_controller.get_all_students(search)

@router.get("/{student_id}", response_model=StudentResponse, status_code=status.HTTP_200_OK)
def read_student(student_id: int):
    return student_controller.get_student_by_id(student_id)

@router.post("/", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate):
    return student_controller.create_student(student)

@router.put("/{student_id}", response_model=StudentResponse, status_code=status.HTTP_200_OK)
def update_student(student_id: int, student_update: StudentUpdate):
    return student_controller.update_student(student_id, student_update)

@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int):
    return student_controller.delete_student(student_id)