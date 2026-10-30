from fastapi import HTTPException, Response, status
from models.student import StudentCreate, StudentUpdate

# In-memory database (Python List)
fake_db = []
id_counter = 1

def get_all_students(search: str = None):
    if search:
        filtered = [s for s in fake_db if search.lower() in s["name"].lower() or search.lower() in s["course"].lower()]
        return filtered
    return fake_db

def get_student_by_id(student_id: int):
    for student in fake_db:
        if student["id"] == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

def create_student(student: StudentCreate):
    global id_counter
    new_student = student.dict()
    new_student["id"] = id_counter
    fake_db.append(new_student)
    id_counter += 1
    return new_student

def update_student(student_id: int, student_update: StudentUpdate):
    stored_student = get_student_by_id(student_id)
    update_data = student_update.dict(exclude_unset=True)
    
    for key, value in update_data.items():
        stored_student[key] = value
        
    return stored_student

def delete_student(student_id: int):
    stored_student = get_student_by_id(student_id)
    fake_db.remove(stored_student)
    # Requirement: 204 No Content with empty body
    return Response(status_code=status.HTTP_204_NO_CONTENT)