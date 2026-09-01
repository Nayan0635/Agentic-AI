# for vscode terminal
from google import genai
from google.genai import types
from dotenv import load_dotenv

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools import tools
from functions import *

load_dotenv()

client = genai.Client(api_key=os.getenv("gemini_key"))
print('connected')
gemini_tools = types.Tool(
    function_declarations=tools
)

config = (
    tools=[gemini_tools], #>>>>file name 
    temperature=0
)

while True:
    _prompt = input("You: ")
    if _prompt.lower() == 'exit':
        print('Cya! have a good Day')
        exit(0)
    responses = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=f'''
        -you will insert new student record, update, delete and show all records
        -apart from these say i can't help with that
        -Prompt: {_prompt}
        ''',
        config = {
            'tools': tools
        }
    )
    tool_calls = []

    for part in responses.candidates[0].content.parts:
        if part.function_call:
            tool_calls.append(part.function_call)

    if tool_calls:
        function_call = tool_calls[0]

        tool_name = tool_calls.name
        tool_args = tool_calls.args

        if tool_name == 'showAll':
            answer = showAll()
        elif tool_name == 'addNew':
            answer = addNew(
                tool_args['name'],
                tool_args['email']
            )
        elif tool_name == 'update':
            answer = update(
                tool_args['id'],
                tool_args['name'],
                tool_args['email']
            )
        elif tool_name == 'delete':
            answer = delete(
                tool_args['id']
            )
        print("I'm using ", tool_name)
        print("Agent: ", answer)
    else:
        print("Agent: Sorry I can't help with that.")