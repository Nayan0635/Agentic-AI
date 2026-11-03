from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.agent_routes import agentRouter
app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_credentials=True,
                   allow_headers=['*'],
                   allow_origins=['*'],
                   allow_methods=['*'])
@app.get("/")
def home():
    return {"message":"welcome to AI Driven API"}
app.include_router(agentRouter)