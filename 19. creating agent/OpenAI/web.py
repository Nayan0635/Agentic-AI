import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

from tools import tools
from functions import *


load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


st.set_page_config(
    page_title="My AI Agent",
    page_icon="🤖"
)

st.title("🤖 My AI Agent")
st.caption("Math + File Assistant")


# -----------------------------
# Chat History
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# -----------------------------
# User Input
# -----------------------------

user_input = st.chat_input("Ask me something...")


if user_input:

    # Show user message
    with st.chat_message("user"):
        st.write(user_input)

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })


    # -----------------------------
    # Connect to LLM
    # -----------------------------

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=1,
        messages=[
            {
                "role": "system",
                "content": """
You are a Math expert who can use addition or multiplication
tools for calculation.

You are also a File Expert who can read and save files
to the local file hello.txt.

Use the available tools whenever they are appropriate.
"""
            },
            *st.session_state.messages
        ],
        tools=tools
    )


    message = response.choices[0].message


    # -----------------------------
    # Tool Calling
    # -----------------------------

    if message.tool_calls:

        tool_call = message.tool_calls[0]

        tool_name = tool_call.function.name
        tool_args = json.loads(tool_call.function.arguments)


        if tool_name == "addNumbers":
            result = addNumbers(
                tool_args["a"],
                tool_args["b"]
            )

        elif tool_name == "multiplyNumbers":
            result = multiplyNumbers(
                tool_args["a"],
                tool_args["b"]
            )

        elif tool_name == "saveFile":
            result = saveFile(
                tool_args["content"]
            )

        elif tool_name == "readFile":
            result = readFile()

        else:
            result = "Unknown tool"


        # Display tool result
        with st.chat_message("assistant"):
            st.write(result)

        st.session_state.messages.append({
            "role": "assistant",
            "content": str(result)
        })


    else:

        # Normal AI response
        answer = message.content

        with st.chat_message("assistant"):
            st.write(answer)

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })