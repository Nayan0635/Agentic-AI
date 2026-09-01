from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os
import json
from tools import tools
from functions import *

load_dotenv()
client = OpenAI(api_key=os.getenv("openai_key"))
# print("Connected to OpenAI")
st.title("🤖 DB Agent :")
textInput = st.text_area("Ask:")
sendBtn   = st.button("Submit")

if sendBtn:
    # Connect to LLM i.e OpenAI.
    responses = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0,
        messages= [
            {
                'role': 'user', 'content': f'''
                -you will insert new student record, upadte, delete and show all records
                -apart from these say i can't help with that
                -Prompt: {textInput}
                '''
            }
        ],
        tools=tools # Here we are attatching our python tools.
    )
    # Check whether OpenAI is using our defined tools or not.
    msg = responses.choices[0].message
    if msg.tool_calls:
        tool_name = msg.tool_calls[0].function.name
        tool_args = json.loads(msg.tool_calls[0].function.arguments)

        if tool_name == 'showAll':
            answer = showAll()
        elif tool_name == 'addNew':
            answer = addNew(tool_args['name'], tool_args['email'])
        elif tool_name == 'update':
            answer = update(tool_args['id'], tool_args['name'], tool_args['email'])
        elif tool_name == 'delete':
            answer = delete(tool_args['id'])
        with st.container(border=True):
            st.subheader("🤖 Agent Response")
            st.write("🔧 Tool Used:", tool_name)
            # Display JSON properly 
            if tool_name == "showAll":
                st.code(answer, language="json")
            else:
                st.success(answer)
    else:
        st.warning("Agent Reply : Sorry I can't help with that")
