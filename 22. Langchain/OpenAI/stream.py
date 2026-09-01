from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import streamlit as st
from langchain_core.prompts import PromptTemplate
#for reading from .env file
load_dotenv()

#Connect to LLM.
llm = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    model="gpt-4.1-mini",
    temperature=1
)
print("OpenAI Connected via LangChain")

#Streamlit GUI Application goes here
st.title("LangChain Customized AI ChatBot : Online Python Teacher:")
textAreaObj = st.text_area("Enter Your Prompt:")
sendBtn     = st.button("Send !")
if sendBtn:
    st.write("Button clicked")
    prompt = PromptTemplate.from_template(f'''
    -You are an AI Python teacher who can only answer related to Python , React, Angular, PHP
    -Apart from these please reply "I can only teach You about Python , React, Angular, PHP ".
    -Prompt :{textAreaObj}
    ''')
    chain = prompt | llm
    responses = chain.invoke({"question":prompt})
    st.write("Agent :",responses.text)
#     prompt = PromptTemplate.from_template(f'''
#     -You are an AI Python teacher who can only answer related to Python
#     -Apart from Python , Django ,flash , fastAPI please reply "I can only teach You python ".
#     -Prompt :{textAreaObj}
#      ''')

