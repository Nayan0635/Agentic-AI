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