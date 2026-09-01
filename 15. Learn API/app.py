#import fastAPI
from fastapi import FastAPI
#loading cors lib
from fastapi.middleware.cors import CORSMiddleware

#Create an Instance of FastAPi class.
app = FastAPI()

#Create a Static Data
users = [
    {"id":1,"name":"mik","age":31,"gender":"Male"},
    {"id":2,"name":"tyson","age":33,"gender":"Female"},
    {"id":3,"name":"emily","age":23,"gender":"Male"},
    {"id":4,"name":"troy","age":24,"gender":"Male"}
]
#CORS Configuration Cross Origin resource sharing option disabled.
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get("/")
def home():
    return {'message':'Welcome to FastAPI'}


@app.get("/api/users")
def all_users():
    return users

@app.get("/api/count")
def user_count():
    return {
        "count": len(users)
    }
    
@app.get("/api/users/{uid}")
def getUser(uid:int):
    flag=True
    for user in users:
        if user.get("id") == uid:
            return user
        else:
            flag=False
    if not flag :
        return {"message":"no user found"}

@app.get("/api/show/")
def getUserByAge(l1:str,l2:str):
    data = [] #empty list
    for user in users:
        if user.get("age")>=int(l1) and user.get("age")<=int(l2):
            data.append(user)
    if not data :
        return {"message":"no user found"}
    else:
        return data



# pip install fastapi uvicorn
# Run : uvicorn app1:app --reload --port 3000
# python -m uvicorn app:app --reload --port 3000
