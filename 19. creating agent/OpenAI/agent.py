from openai import OpenAI
from dotenv import load_dotenv
import os
import json
from tools import tools
from functions import *
#for reading from .env file
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
   
)
print("Connected to OpenAI")

#ChatLoop
while True:
    user_input = input("You:")
    if user_input.lower()=='exit':
        print("Agent:Bye Bye")
        exit(0)
    #Connect to LLM.
    responses = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=1,
        messages=[
            {
                "role":"user",
                "content":f'''
                 -You are a Math expert who can use addition or multipication tools for calculation.
                 -You are a File Expert who can read & save file to local file i.e hello.txt
                 -User Prompt :{user_input}
'''
            }
        ],
        tools=tools #Here Ai is using the tool.
    )
    #Check whether AI is using our tools or not.
    message = responses.choices[0].message
    if message.tool_calls:
        tool_name = message.tool_calls[0].function.name
        tool_args = json.loads(message.tool_calls[0].function.arguments)
        print("Agent is using tool :",tool_name)
        if tool_name == "addNumbers":
            result = addNumbers(tool_args['a'],tool_args['b'])
        elif tool_name =="multiplyNumbers":
            result = multiplyNumbers(tool_args['a'],tool_args['b'])
        elif tool_name == "saveFile":
            result = saveFile(tool_args['content'])
        elif tool_name == "readFile":
            result = readFile()
        print("Agent Reply :",result)
    else:
        print("Agent : Sorry I can't help with that.")