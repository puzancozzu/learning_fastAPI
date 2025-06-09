from fastapi import FastAPI
from typing import Optional

app = FastAPI()

students ={
    1: {"name": "John", "age": 20, "grade": "A"},
    2: {"name": "Jane", "age": 22, "grade": "B"},
}


### have both query and parameter - student_id is parameter where as name and age are query parameters
@app.get("/get_by_name_QnP/{student_id}")
def get_student_by_name(student_id: int, name: Optional[str] = None, age: Optional[int] = None):
    student = students.get(student_id)
    if student and (name is None or student["name"] == name):
        return student
    return {"message": "Student not found"}