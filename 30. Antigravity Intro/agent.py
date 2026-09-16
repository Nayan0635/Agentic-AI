#Agent -> Creating and Building AI Agents.
#LocalAgentConfig => let tools to be attached with AI.
from google.antigravity import Agent,LocalAgentConfig
from tools import *
from dotenv import load_dotenv
import os
import asyncio
load_dotenv()

#Here we need to create an configuration object for Antigravity tools.
configObj = LocalAgentConfig(
    # api_key=os.getenv("gemini_key"),
    # model="gemini-3.1-flash-lite",
    api_key=os.getenv("openai_key"),
    model="gpt-4.1-mini",
    tools=[addNumbers,multiNumbers,saveFile,readFile] #tools are binded.
) 
print("Antigravity is connected")

#available tools 
available_tools={
        "addNumbers": addNumbers,
        "multiNumbers": multiNumbers,
        "saveFile" : saveFile,
        "readFile" : readFile
    }

#Create an asynchronous function for communicating with Gemini LLM.
async def callAgent():
    async with Agent(config=configObj) as agent:

        while True:

            user_input = input("You : ")

            if user_input.lower() in ["exit", "quit"]:
                print("Agent : Bye Bye")
                return

            responses = await agent.chat(user_input)

            async for tool in responses.tool_calls:

                toolName = tool.name
                toolArgs = tool.args

                print("Tool :", toolName)
                print("Arguments :", toolArgs)
                if toolName == "readFile":
                    result = available_tools[toolName](**{})
                else:      
                    result = available_tools[toolName](**toolArgs)

                print("Agent Response :", result)


#MainScript
if __name__ == "__main__":
    asyncio.run(main=callAgent())
