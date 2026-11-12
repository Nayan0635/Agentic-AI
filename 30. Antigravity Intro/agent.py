from google.antigravity import Agent,LocalAgentConfig
from tools import *
from dotenv import load_dotenv
import os
import asyncio
load_dotenv()

#agent config
agent_config = LocalAgentConfig(
    api_key=os.getenv("openai_key"),
    model="gpt-4.1-mini",
    tools=[addNumbers,multiNumbers,saveFile,readFile] #tools are binded.
)

tool_registry={
        "addNumbers": addNumbers,
        "multiNumbers": multiNumbers,
        "saveFile" : saveFile,
        "readFile" : readFile
}

#Create an asynchronous function for communicating with Gemini LLM.
async def runAgent():
    async with Agent(config=agent_config) as agent:
        while True:
            user_input = input("You : ")
            if user_input.lower() in ["exit", "quit"]:
                print("Agent : Bye Bye")
                break

            responses = await agent.chat(user_input)

            async for tool in responses.tool_calls:

                tool_name = tool.name
                tool_args = tool.args

                print("Tool :", tool_name)
                print("Arguments :", tool_args)
                try:      
                    result = tool_registry[tool_name](**tool_args)
                except Exception as e:
                    print("Tool Error: ", e)
                print("Agent Response :", result)

if __name__ == "__main__":
    asyncio.run(main=runAgent())
