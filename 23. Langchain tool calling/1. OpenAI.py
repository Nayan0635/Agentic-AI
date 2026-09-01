from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from tools import *


#start fetching from .env file
load_dotenv()

#connect to llm.
llm = ChatOpenAI(
    api_key=os.getenv("openai_key"),
    model="gpt-4.1-mini",
    temperature=1
)
print("OpenAi connected")

#Binding the tools with the llm.
llm = llm.bind_tools([addNumbers,multiplyNumbers,saveFile,readFile, total, avg, gradation])

#ChatLoop
while True:
    user_input = input("You :")
    if user_input.lower()=='exit' or user_input.lower()=='quit':
        print("Agent :Bye Bye")
        exit(0)
    #Communicate with the llm.
    responses = llm.invoke(f'Question : {user_input}')
    #Here we need to check whether openai is using our defined tools or not.
    if responses.tool_calls:
        tool_name = responses.tool_calls[0]['name']
        tool_args = responses.tool_calls[0]['args']

        if tool_name == "addNumbers":
            result = addNumbers.invoke(tool_args)
        elif tool_name == "multiplyNumbers":
            result = multiplyNumbers.invoke(tool_args)
        elif tool_name == "saveFile":
            result = saveFile.invoke(tool_args)
        elif tool_name =='readFile':
            result = readFile.invoke(tool_args)
        elif tool_name == "total":
            result = total.invoke(tool_args)
        elif tool_name == "avg":
            result = avg.invoke(tool_args)
        elif tool_name =='gradation':
            result = gradation.invoke(tool_args)
        elif tool_name =='score': #need good prompt to pick it
            result = score.invoke(tool_args)
            
        print("Agent is using-> ",tool_name)
        print("Agent Response :",result)
    else:
        print("Agent : Sorry I cann't help with that.")