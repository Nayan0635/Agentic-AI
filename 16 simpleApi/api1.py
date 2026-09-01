#import fastAPI
from fastapi import FastAPI
#loading cors lib
from fastapi.middleware.cors import CORSMiddleware
from routes.user import userRouter as user_router
#Create an Instance of FastAPi class.
app = FastAPI()



#CORS Configuration Cross Origin resource sharing option disabled.
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


#Here we include the router
app.include_router(user_router)
@app.get("/")
def home():
    return {'message':'Welcome to FastAPI'}




            
        
    