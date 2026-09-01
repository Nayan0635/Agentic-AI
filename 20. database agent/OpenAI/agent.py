# for vscode terminal
from openai import OpenAI
from dotenv import load_dotenv
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools import tools
from functions import *

load_dotenv()

client = OpenAI(api_key=os.getenv("openai_key"))

while True:
    _prompt = input("You: ")
    if _prompt.lower() == 'exit':
        print('Cya! have a good Day')
        exit(0)
        
    responses = client.chat.completions.create(
        model= 'gpt-4.1-mini',
        temperature= 0,
        messages= [
            {
                'role': 'user', 'content': f'''
                -you will insert new student record, upadte, delete and show all records
                -apart from these say i can't help with that
                -Prompt: {_prompt}
                '''
            }
        ],
        tools = tools
    )
    msg = responses.choices[0].message
    if msg.tool_calls:
        tool_name = msg.tool_calls[0].function.name
        tool_args = json.loads(msg.tool_calls[0].function.arguments) #>>json.loads
        
        if tool_name == 'showAll':
            answer = showAll()
        if tool_name == 'addNew':
            answer = addNew(tool_args['name'], tool_args['email'])
        if tool_name == 'update':
            answer = update(tool_args['id'], tool_args['name'], tool_args['email'])
        if tool_name == 'delete':
            answer = delete(tool_args['id'])
        print("I'm using ",tool_name)
        print("Agent: ",answer)
    else:
        print("Agent: Sorry I can't help with that.")