from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from students_routes import studentRouter
app = FastAPI()

#Making the server cors free.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message":"welcome to student api"}

app.include_router(studentRouter)

