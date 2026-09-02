import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from function import sendMail
from langchain_core.prompts import PromptTemplate

load_dotenv()

# Connecting to LLM
llm = ChatOpenAI(
    api_key=os.getenv("openai_key"),
    model="gpt-4.1-mini",
    temperature=1
)
llm = llm.bind_tools([sendMail])
# Streamlit UI
st.title("Smart Mail Agent")

user_input = st.text_area("Enter your message:")

if st.button("Submit"):
    if user_input.strip():
        # Create Prompt
        prompt = PromptTemplate(
            template="""
                Please modify the body of the email intelligently.
                Rules:
                - Make the message professional and polite.
                - Correct grammar and spelling.
                - Keep the message short and meaningful.
                - Do not change the original intention.
                - Then send the email using the sendMail tool.
                User's request:{user_input}
            """,
            input_variables=["user_input"]
        )
        myMessages = prompt.invoke({
            "user_input": user_input
        })
        # Connected to LLM
        response = llm.invoke(myMessages)

        if response.tool_calls:
            tool_name = response.tool_calls[0]["name"]
            tool_args = response.tool_calls[0]["args"]

            if tool_name == "sendMail":
                result = sendMail.invoke(tool_args)

                st.success("Email sent successfully!")
                st.write(result)
        else:
            st.warning(
                "Sorry, I can only help with sending smart messages through mail."
            )
    else:
        st.warning("Please enter a message.")
