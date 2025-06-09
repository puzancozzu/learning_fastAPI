from fastapi import FastAPI, Path

app = FastAPI()

students ={
    1: {"name": "John", "age": 20, "grade": "A"},
    2: {"name": "Jane", "age": 22, "grade": "B"},
}


### Define a route to get a student by Name - Query Parameter
### This route will return the student details if the name is found in the database
### Query : /get_by_name/results?name=John

@app.get("/get_by_name")
def get_student_name(name: str):   
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
        
    return {"message": "Student not found"}     ## if not found, return a message


###  in above implemetation we need to pass the argument of type String in the url 
###   but in this by default None - it is not mandatory to pass the argument in the url,
###       - so by defualt it will return {"message" : " ..... "}
### -- not good method at all 
@app.get("/get_by_name_none")
def get_student_name_none(name: str = None):   ## None
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]  
    return {"message": "Student not found"} 


### pass a defualt argument in the url
from typing import Optional
@app.get("/get_by_name_optional")
def get_student_name_optional(name: Optional[str] = None,):    ## Optional[str] = None - Not Required will be optional
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]  
    return {"message": "Student not found"} 


### for multiple paramters 
### age- is not used in logic
@app.get("/get_by_multiple_para")
def get_student_multiple_para(*, name: Optional[str] = None, age : int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]  
    return {"message": "Student not found"} 

''' 
    (name: Optional[str] = None, age : int) - thorws error -"Required" parameter "age" ,
        cannot be after optional parameter "name" 
    ( age : int, name: Optional[str] = None,) - this will do the work but above one is effecient one 
        
'''