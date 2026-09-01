import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

#Connecting to OpenAI LLM.
client = OpenAI(api_key=os.getenv("openai_key"))
print("Connected to OpenAI")

#GUI using Streamlit
st.title("WebBot Personal Python Teacher :")
textInput = st.text_area("Question:")
sendBtn   = st.button("Submit")
if sendBtn:
    responses = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=1,
        messages=[
             {
                "role":"system","content":'''
                 -You are an AI expert Customized ChatBot who will only answer about EjobIndia like courses , fees , placements etc.
                 -Your Name is "EjobBot max"
                 -Apart from EjobIndia related Please reply "I can only assist with Ejobindia related queries".
                 '''
            },
            
            # {
            #     "role":"system","content":'''
            #      -You are an AI expert who can only answer about Technical Programming Languages like Angular,React ,Java and Python.
            #      -Your Name is "bot"
            #      -Created & Maintained By EjobIndia.
            #      -Apart from mentioned technical programming languages Please reply "I can only assist with  Angular, React , Java and Python related queries".
            #      '''
            # },
            
            # {
            #     "role":"system","content":'''
            #      -You are an AI expert who can only answer from Python related queries.
            #      -Your Name is "PythonAI Pro"
            #      -Created & Maintained By EjobIndia.
            #      -Apart from Python Please reply "I can only assist with Python related queries".
            #      '''
            # },
             {
                 "role":"user","content":textInput
             }
        ]
    )
    msg = responses.choices[0].message.content
    st.write("Bot Reply :",msg)


# streamlit run webBot.py
