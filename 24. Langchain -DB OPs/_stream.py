import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from tools import *

load_dotenv()

# connect to llm
llm = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    model="gpt-4.1-mini",
    temperature=0
)

# binding the llm with specified tools
llm = llm.bind_tools([
    addNewUser,
    getUser,
    getAllUsers,
    deleteUser,
    updateUser
])

tools_by_name: dict = {
    "addNewUser": addNewUser,
    "getAllUsers": getAllUsers,
    "getUser": getUser,
    "deleteUser": deleteUser,
    "updateUser": updateUser
}


st.title("DB Agent")

textArea = st.text_area("Question :")
sendBtn = st.button("Submit")

if sendBtn:

    responses = llm.invoke(f'''
    Prompt : {textArea}
    ''')

    if responses.tool_calls:

        tool_name = responses.tool_calls[0]["name"]
        tool_args = responses.tool_calls[0]["args"]

        st.write("Agent is using tool :", tool_name)

        result = tools_by_name.get(tool_name).invoke(tool_args)

        st.write("Agent Response :", result)

    else:
        st.write("Agent : Sorry I cann't help with that.")