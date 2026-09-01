from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from tools import *


# start fetching from .env file
load_dotenv()

# connect to GitHub Models
llm = ChatOpenAI(
    api_key=os.getenv("github_token"),
    base_url="https://models.github.ai/inference",
    model="openai/gpt-4.1-mini",
    temperature=1,
)

print("GitHub Models connected")


# Binding the tools with the llm
llm = llm.bind_tools([
    addNumbers,
    multiplyNumbers,
    saveFile,
    readFile,
    total,
    avg,
    gradation
])


# ChatLoop
while True:

    user_input = input("You : ")

    if user_input.lower() == "exit" or user_input.lower() == "quit":
        print("Agent : Cya have a good day")
        exit(0)

    # Communicate with the LLM
    response = llm.invoke(f"Question : {user_input}")

    # Check whether the LLM wants to use our defined tools
    if response.tool_calls:

        tool_name = response.tool_calls[0]["name"]
        tool_args = response.tool_calls[0]["args"]

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

        print("Agent is using ->", tool_name)
        print("Agent Response :", result)

    else:
        print("Agent :", response.content)