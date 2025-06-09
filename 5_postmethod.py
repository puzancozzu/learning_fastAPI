from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel


### POST - method used to create a new data 
app = FastAPI()


### data we have in data base (this dict is out data base) named - students
students = {
    1 : {"name": "John", "age": 20 , "grade": 9},
    2: {"name": "Jane", "age": 21, "grade": 10},
}


### this is the model of our data (this is how we want to see our data) - similar structure that we have in data base
class Student(BaseModel):
    name : str
    age : int
    grade : int


### this is the endpoint for POST method 
### {student_id} - path parameter - user will enter 
### student - body parameter -
#       - user will enter data in body of request - 
#       - stored in student variable - have structure of class Student
### store - JSON - data  in data base(students) - student_id(key) : student(value)

@app.post("/create_student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"error": "Student ID already exists."}
    students[student_id] = student.dict() ## convert student - pydantic model  to dict

    return students[student_id]



### check if added student details shown or not 
@app.get("/get_student/{student_id}")    ## ----- Path Parameter-----
def get_student(student_id: int):
    return students[student_id]