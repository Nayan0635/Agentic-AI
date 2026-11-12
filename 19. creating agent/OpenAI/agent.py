from openai import OpenAI
from dotenv import load_dotenv
import os
from tools import tools
from functions import *
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
print("key found")

#ChatLoop
while True:
    user_input = input("You:")
    if user_input.lower()=='exit':
        print("Agent: cya!")
        exit(0)
    #Connect to LLM.
    responses = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature= 0.3,
        message = [
            {
                "role" : "system",
                "content" : '''
                    -You are a Math expert who can perform addition of 2 numbers.
                    -You are a File Expert Agent who can save & read content from created file .
                '''
            },
            {
                "role": "user",
                "content": f"User prompt: {user_input}",
            }
        ],
        tools= tools
    )

    #Here we need to check whether Gemini is using our defined tools or not.
    message = responses.choices[0].message
    if message.tool_calls:
        
        tool_name = message.tool_calls[0].function.name
        tool_args = json.loads(message.tool_calls[0].function.arguments)
        
        if tool_name == "addNumbers":
            result = addNumbers(tool_args['a'],tool_args['b'])
        if tool_name == "multiplyNumbers":
            result = multiplyNumbers(tool_args['a'],tool_args['b'])
        elif tool_name == "multiplyNumbers":
            result = multiplyNumbers(tool_args['a'],tool_args['b'])
        
        print("Agent :",result)
    else:
        print("Sorry I can either help with addition of file read & write automations")
            