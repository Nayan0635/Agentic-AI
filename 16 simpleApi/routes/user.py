from fastapi import APIRouter,Request
 
userRouter = APIRouter(
    prefix="/api/users",
    tags=['Users'],
     
)

#Create a Static Data 
users = [
    {"id":1,"name":"Soumik","age":31,"gender":"Male"},
    {"id":2,"name":"Suchismita","age":33,"gender":"Female"},
    {"id":3,"name":"Nayan","age":23,"gender":"Male"},
    {"id":4,"name":"Zaid","age":24,"gender":"Male"}
]


#All user's related routes are mentioned below
@userRouter.get("/")
def all_users():
    return users


    

@userRouter.get("/{uid}")
def getUser(uid:int):
    flag=True
    for user in users:
        if user.get("id") == uid:
            return user
        else:
            flag=False 
    if not flag :
        return {"message":"no user found"}

@userRouter.get("/api/show/")
def getUserByAge(l1:str,l2:str):
    data = [] #empty list
    for user in users:
        if user.get("age")>=int(l1) and user.get("age")<=int(l2):
            data.append(user)
    if not data :
        return {"message":"no user found"}
    else:
        return data

#Select and count all male candidates
#Select and count all Female candidates
#Sum , Average of all ages 
#Max age holder Most senior User
#Min Age Holder Junior user.




@userRouter.post("/signup")
async def signup(request:Request):
    data = await request.json()
    #return data
    name = data.get("name")
   
    age  = int(data['age'])
    gender=data.get("gender")

    #appending to exisiting Data source
    users.append( {
         "name":name,
        
         "age":age,
         "gender":gender
    })
    return {
        "message":"User added successfully",
        "users":users
    }
@userRouter.put("/update/{uid}")
async def updateUser(uid:int,request:Request):
    data = await request.json()
    newName = data.get("name")
    newAge  = data.get("age")
    newGender=data.get("gender")
    user = getUser(uid=uid)
    if user:
     if not newName :
        newName = user['name']
     if not newAge:
        newAge = user['age']
     if not newGender:
        newGender = user['gender']

     user['name'] = newName
     user['gender']=newGender
     user['age']   = newAge
     return {"message":"User Profile successfully updated","users":users}   
     
@userRouter.delete("/delete/{uid}")
def deleteUser(uid:int):
    user =getUser(uid=uid)
    if not user:
        return {"message":"invalid user id"}
    else:
        users.remove(user)
        return {"message":"Delete successfully","users":users}
    

print("user router is working")