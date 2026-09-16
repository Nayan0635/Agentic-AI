from google.antigravity import LocalAgentConfig,Agent
from dotenv import load_dotenv
from crud import *
import os
import asyncio
load_dotenv()

config= LocalAgentConfig(
    api_key=os.getenv("GOOGLE_API_KEY"),
    model="gemini-3.1-flash-lite",
    tools=[addNewStudent,getAllStudents,getStudent]
)

available_tools ={
    "getStudent":getStudent,
    "getAllStudents":getAllStudents,
    "addNewStudent" :addNewStudent
}

async def callAgent():
    async with Agent(config=config) as agent:
        while True:
            user_input = input("You:")
            if user_input.lower()=='exit':
                print("Agent: Bye Bye")
                return
            responses = await agent.chat(user_input)
            #Check whether AI is using tools or not.
            async for tool in responses.tool_calls:
                toolName = tool.name
                toolArgs = dict(tool.args)
                print("Agent is using tool :",toolName)
                if toolName == "getAllStudents":
                    result = available_tools.get(toolName)()
                else:    
                    result = available_tools.get(toolName)(**toolArgs) 
                print("Agent Response :",result)

#MainScript
if __name__ == "__main__":
    asyncio.run(main=callAgent())