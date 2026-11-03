from openai import OpenAI
from dotenv import load_dotenv
import os
from fastapi.routing import APIRouter
from fastapi.requests import Request
from tools import tools
from crud import *
import json
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

agentRouter = APIRouter(
    prefix="/api/agent",
    tags=['agentRouter']
)
@agentRouter.post("/chat")
async def agentChat(request:Request):
    data:dict = await request.json()
    question = data.get("question")
    #Connecting to OpenAI
    responses = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role":"user","content":question}
        ],
        tools=tools
    )
    #Now to check whether OpenAI is using defined tools or not
    message = responses.choices[0].message
    if message.tool_calls:
        toolName = message.tool_calls[0].function.name
        toolArgs = json.loads(message.tool_calls[0].function.arguments)
        if toolName== "addNewPost":
            result = addNewPost(toolArgs['title'],toolArgs['desc'])
        elif toolName=="getAllPosts":
            result = getAllPosts()
        elif toolName == "updatePost":
            result = updatePost(
            toolArgs["title"],
            toolArgs["desc"],
            toolArgs["post_id"])
        elif toolName == "deletePost":
            result = deletePost(toolArgs["post_id"])
        return {"Agent":result, "tool":toolName,"args":toolArgs}
    else:
        return {"Agent":"Sorry I can only help with Database Automation"}

# python -m uvicorn main:app --reload
