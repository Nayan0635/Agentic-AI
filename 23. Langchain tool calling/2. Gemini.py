from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from tools import *
load_dotenv()
#Connected to Google Gemini
llm = ChatGoogleGenerativeAI(
  api_key=os.getenv("gemini_key"),
  model="gemini-3.1-flash-lite",
   
)
print("Hello! I'm Gemini Agent")

#Binding the llm with tools
llm = llm.bind_tools([addNumbers,multiplyNumbers,saveFile,readFile, total, avg, gradation, score])

#ChatLoop
while True:
    user_input = input("You:")
    if user_input.lower()=='exit':
        print("Agent : Bye Bye")
        exit(0)
    #Connected to llm.
    responses = llm.invoke(f'''
    -Question :{user_input}
''')
    #Here we need to check whether gemini is using defined tools or not
    if responses.tool_calls:
        tool_name = responses.tool_calls[0]['name']
        tool_args = responses.tool_calls[0]['args']
        
        if tool_name =="addNumbers":
            result = addNumbers.invoke(tool_args)
        elif tool_name == "multiplyNumbers":
            result = multiplyNumbers.invoke(tool_args)
        elif tool_name =="saveFile":
            result = saveFile.invoke(tool_args)
        elif tool_name =="readFile":
            result= readFile.invoke(tool_args)
        elif tool_name =="total":
            result = total.invoke(tool_args)
        elif tool_name == "avg":
            result = avg.invoke(tool_args)
        elif tool_name =="gradation":
            result = gradation.invoke(tool_args)
        elif tool_name =="score":
            result= score.invoke(tool_args)
            
        print("Agent is using tool :",tool_name)
        print("Agent Response :",result)
    else:
        print("Agent : Sorry I cann't help with that")