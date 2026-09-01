from openai import OpenAI #importing openai module
from dotenv import load_dotenv #importing dotenv for reading through .env file
import os #Grant OS Permission

#Now it has started to fetching from .env file
load_dotenv()

#print(os.getenv("openai_key"))

#Connecting to LLM i.e OpenAI.

client = OpenAI(api_key=os.getenv("openai_key"))
print("Connected to OpenAI")

#We will create a ChatLoop where user can interact with LLM.
while True:
    user_input = input("enter prompt :")
    if user_input.lower()=='exit':
        print("Bot : Cya! Have a great day!")
        exit(0)
    #Connect to llm.
    responses = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=1, #Creative answer by AI
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
            #      -Created & Maintained By me.
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
                "role":"user","content":user_input
            }
        ]
    )
    msg = responses.choices[0].message.content
    print("Bot Reply :",msg)
