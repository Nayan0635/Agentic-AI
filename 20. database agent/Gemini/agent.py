import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Parent directory import for functions.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from functions import *
from tools import tools

load_dotenv()

client = genai.Client(api_key=os.getenv("gemini_key"))
print("Gemini Connected")

# Wrap declarations properly for google-genai SDK
config = types.GenerateContentConfig(
    tools=[types.Tool(function_declarations=tools)],
    temperature=0
)

# ChatLoop
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Agent: Bye Bye")
        exit(0)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
        - You will insert new student record, update, delete and show all records.
        - Apart from these say i can't help with that.
        User Prompt: {user_input}""",
        config=config
    )

    message = response.candidates[0]
    
    # Check for function calls safely across response parts
    function_calls = [part.function_call for part in message.content.parts if part.function_call]

    if function_calls:
        fc = function_calls[0]
        tool_name = fc.name
        tool_args = dict(fc.args) if fc.args else {}
        print("Agent detected tools :", tool_name)

        if tool_name == "showAll":
            result = showAll()
        elif tool_name == "addNew":
            result = addNew(tool_args.get("name"), tool_args.get("email"))
        elif tool_name == "update":
            result = update(tool_args.get("id"), tool_args.get("name"), tool_args.get("email"))
        elif tool_name == "delete":
            result = delete(tool_args.get("id"))

        print("Agent :", result)
    else:
        print("Agent: Sorry I can't help with that.")