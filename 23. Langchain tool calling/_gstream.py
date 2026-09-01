import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from tools import *



load_dotenv()

#connect to llm.
llm = ChatGoogleGenerativeAI(
    api_key=os.getenv("gemini_key"),
    model="gemini-3.1-flash-lite",
)
print("gemini connected")

#Binding the tools with the llm.
llm = llm.bind_tools([addNumbers,multiplyNumbers,saveFile,readFile, total, avg, gradation, score])
#Quickly create a small effective gui using streamlit

st.title("ArithMetic & File Agent :")
textArea = st.text_area("Question :")
sendBtn = st.button("Submit")

if sendBtn:
    _prompt = textArea
     #Communicate with the llm.
    responses = llm.invoke(f'''
          Question : {_prompt}
        ''')
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
            elif tool_name =='score':
                result = score.invoke(tool_args)
                 
            st.write("Agent is using tool :",tool_name)
            st.write("Agent Response :",result)
    else:
            st.write("Agent : Sorry I cann't help with that.")