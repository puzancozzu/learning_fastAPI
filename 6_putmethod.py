### PUT - used to update what already exist

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1 : {"name": "John", "age": 20 , "grade": 9},
    2: {"name": "Jane", "age": 21, "grade": 10},
    3: {"name": "Bob", "age": 19, "grade": 8},
}


### we are using optional here, cause we may or may not update eveything
### if not declared as optional, it will throw an error if not provided (is it must required)
### so declaring them as optional, if data avlaible it will update else it will not throw an error - remains as it is no updates 
class UpdatedStudent(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    grade : Optional[int] = None

@app.put("/update_students/{student_id}")
def update_students(student_id: int, student: UpdatedStudent):
    ## if given id exist in data  bae (json) or not
    if student_id not in students:
        return {"error": "Student not found"}  
    
    students[student_id] = student.dict()
    return students[student_id]


### check if added student details updated or not
@app.get("/get_student/{student_id}")    
def get_student(student_id: int):
    return students[student_id]


''' 
    In this implementation : while updating any data if we just try to update the specific filed of data - rest is set to null
    For Eg: if we update only "name" : "Bob" ----> "BOB MARLEY" and keep "age and "class" untouched 
    Result : {"name": "BOB MARLEY", "age": null, "grade": null}

'''

@app.put("/update_students_2/{student_id}")
def update_students_2(student_id: int, student: UpdatedStudent):
    ## if given id exist in data  bae (json) or not
    if student_id not in students:
        return {"error": "Student not found"}  

    ## update the data only when they or not None
    if student.name != None:
        students[student_id]["name"] = student.name

    if student.age != None:
        students[student_id]["age"] = student.age    

    if student.grade != None:
        students[student_id]["grade"] = student.grade
    
    # students[student_id] = student.dict()
    return students[student_id] 