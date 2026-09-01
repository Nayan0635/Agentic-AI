from google import genai
from dotenv import load_dotenv
import os
from tools import tools
from functions import *
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)
print("Gemini Connected")

#ChatLoop
while True:
    user_input = input("You:")
    if user_input.lower()=='exit':
        print("Agent:Bye Bye")
        exit(0)
    #Connect to LLM.
    responses = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=f'''
        -You are a Math expert who can perform addition of 2 numbers.
        -You are a File Expert Agent who can save & read content from created file .
        User Prompt :{user_input}''',
config={
    "tools":tools
}
      
    )

    #Here we need to check whether Gemini is using our defined tools or not.
    message = responses.candidates[0]
    if message.content.parts[0].function_call:
        tool_name = message.content.parts[0].function_call.name
        tool_args =dict( message.content.parts[0].function_call.args)
        print("Agent detected tools :",tool_name)
        if tool_name == "addNumbers":
            result = addNumbers(tool_args['a'],tool_args['b'])
        elif tool_name =="saveFile":
            result = saveFile(tool_args['content'])
        elif tool_name == "readFile":
            result = readFile()
        print("Agent :",result)
    else:
        print("Sorry I can either help with addition of file read & write automations")
            