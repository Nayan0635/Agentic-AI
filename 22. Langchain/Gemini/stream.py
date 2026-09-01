from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
#start fetching from .env file
load_dotenv()

#Connect to Google Gemini LLM
llm = ChatGoogleGenerativeAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    model="gemini-2-flash",
    temperature=1
)
print("Gemini Connected")

st.title("LangChain Customized AI ChatBot")
user_prompt = st.text_area("Enter Your Prompt:")
sendBtn = st.button("Send!")

if sendBtn:
    prompt_template = PromptTemplate.from_template("""
    - You are a Python Teacher who can only answer related to Python.
    - Apart from that Please Say I can't help.
    - Question: {question}
    """)

    parser = StrOutputParser()

    chain = prompt_template | llm | parser

    answer = chain.invoke({"question": user_prompt})

    st.write("Agent:", answer)