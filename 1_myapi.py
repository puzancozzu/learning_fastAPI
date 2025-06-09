import fastapi
from fastapi import FastAPI


### initializing the FastAPI application - instance of fastapi object
# FastAPI is a class that we can use to create an API application
app = FastAPI()   

### end point - methods
# GET - get an inforation
# POST - create a new information
# PUT - update an existing information
# DELETE - delete an existing information


### creating a new API - end point (URL path)
# The path is the URL that the user will use to access the API


### get - it is to get the data from the fast api instance
@app.get("/")  #"/" is the root path - home page 

### funtion to get the data 
def index():
    return{"name": "First Data"}  # it use json format to return the data

''' # The above code is a simple FastAPI application that defines a single endpoint at the root path ("/").
    The @app.get("/") decorator is used to define a GET endpoint at the root path.'''

''' # The index function is called when a GET request is made to the root path, 
    and it returns a JSON response with a single key-value pair {"name": "First Data"}.'''

''' # The FastAPI application is created using the FastAPI() class, 
    and it can be run using a command like uvicorn myapi:app --reload.'''

''' # When the application is running, you can access the endpoint by navigating to 
    http://localhost:8000/ in your web browser or using a tool like curl or Postman.'''