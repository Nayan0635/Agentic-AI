from fastapi.routing import APIRouter
from fastapi import Request
from crud import *
studentRouter = APIRouter(
    prefix="/api/students",
    tags=['Students']
)

@studentRouter.post("/add")
async def addingStudent(request:Request):
    data = await request.json()
    message = addNewStudent(data.get("name"),data.get("email"))
    return {"message":message}
 
@studentRouter.get("/all")
def allStudents():
    return getAllStudents()

@studentRouter.get("/show/{sid}")
def getStudentById(sid:int):
    return getStudent(sid)

@studentRouter.put("/update/{uid}")
async def updateStudentById(uid:int,request:Request):
    data = await request.json()
    return updateStudent(sid=uid,name=data.get("name"),email=data.get("email"))

@studentRouter.delete("/delete/{uid}")
def deleteStudentById(uid:int):
    return deleteStudent(sid=uid)
