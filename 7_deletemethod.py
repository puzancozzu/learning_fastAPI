### DELETE - used to delete the data

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1 : {"name": "John", "age": 20 , "grade": 9},
    2: {"name": "Jane", "age": 21, "grade": 10},
    3: {"name": "Bob", "age": 19, "grade": 8},
}

@app.delete("/delete_student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"message": "Student not found"}
    
    del students[student_id]
    return{"meassage ": "Student deleted Successfully"}


### checking for the deletded IDs
@app.get("/get_student/{student_id}")    
def get_student(student_id: int):
    return students[student_id]