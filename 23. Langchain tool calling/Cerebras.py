# import os
# import json
# import re
# from cerebras.cloud.sdk import Cerebras

# # Initialize Cerebras client
# client = Cerebras(
#     api_key=os.environ.get("CEREBRAS_API_KEY"),
# )

from langchain_cerebras import ChatCerebras
from dotenv import load_dotenv
import os
from tools import *


# start fetching from .env file
load_dotenv()


# connect to llm
llm = ChatCerebras(
    api_key=os.getenv("CEREBRAS_API_KEY"),
    model="gpt-oss-120b",
    temperature=1
)

print("Cerebras connected")


# Binding the tools with the llm
llm = llm.bind_tools([
    addNumbers,
    multiplyNumbers,
    saveFile,
    readFile,
    total,
    avg,
    gradation,
    score
])


# ChatLoop
while True:

    user_input = input("You : ")

    if user_input.lower() == "exit" or user_input.lower() == "quit":
        print("Agent : Bye Bye")
        exit(0)


    # Communicate with the LLM
    responses = llm.invoke(f"Question : {user_input}")


    # Check whether Cerebras is using our defined tools
    if responses.tool_calls:

        tool_name = responses.tool_calls[0]["name"]
        tool_args = responses.tool_calls[0]["args"]


        if tool_name == "addNumbers":
            result = addNumbers.invoke(tool_args)

        elif tool_name == "multiplyNumbers":
            result = multiplyNumbers.invoke(tool_args)

        elif tool_name == "saveFile":
            result = saveFile.invoke(tool_args)

        elif tool_name == "readFile":
            result = readFile.invoke(tool_args)

        elif tool_name == "total":
            result = total.invoke(tool_args)

        elif tool_name == "avg":
            result = avg.invoke(tool_args)

        elif tool_name == "gradation":
            result = gradation.invoke(tool_args)

        elif tool_name == "score":
            result = score.invoke(tool_args)


        print("Agent is using ->", tool_name)
        print("Agent Response :", result)


    else:
        print("Agent :", responses.content)
