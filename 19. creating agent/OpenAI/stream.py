from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st
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

#GUI using Streamlit
st.title("🤖My first AI Agent :")
textInput = st.text_area("Query:")
sendBtn   = st.button("Submit")
if sendBtn:
    #Connect to LLM.
    responses = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=1,
        messages=[
            {
                "role":"user",
                "content":f'''
                 -act like Math expert who can use addition or multipication tools for calculation.
                 -You are a File Expert who can read & save file to local file i.e hello.txt
                 -User Prompt :{textInput}
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
        st.write("Agent Reply :", result)
    else:
        st.write("Agent :", message.content)