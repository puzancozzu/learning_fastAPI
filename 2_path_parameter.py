from fastapi import FastAPI

app = FastAPI()

## Sample data to simulate a database
# This dictionary represents a simple in-memory database of students.
students ={
    1: {"name": "John", "age": 20, "grade": "A"},
    2: {"name": "Jane", "age": 22, "grade": "B"},
}


#### Endpoint to get a student by ID
# This endpoint retrieves a student's information based on the provided student ID. 
# The path parameter {student_id} allows the user to specify which student's information they want to retrieve.
@app.get("/get_student/{student_id}")    ## ----- Path Parameter-----

def get_student(student_id: int):
    return students[student_id]


### http://127.0.0.1:8000/get_student/1 - This will return the student with ID 1. - on localhost 
### http://127.0.0.1:8000/docs - This will show the API documentation generated by FastAPI.
### http://127.0.0.1:8000/get_student/2 - This will return the student with ID 2.
### http://127.0.0.1:8000/get_student/3 - This will return an error because there is no student with ID 3 in the sample data.
### Note:
# - The student_id parameter is defined as an integer, so if a non-integer value is provided, FastAPI will automatically return a 
#   422 Unprocessable Entity error.



### Endpoint to get student - addition description is added for clarity - so users know what to enter in the request body
### what parameter to pass to get desired output 
from fastapi import Path
@app.get("/get_student_path/{student_id}")
def get_student_path(student_id: int = Path(..., description="The ID of the student you want to view", gt= 0 , lt = 2)):
    return students[student_id]
 


#### the int value enter as parameter must be greater tha 0 and less than 2.
#### gt, lt, ge, le, range - these are used to define the range of values that the parameter can take
