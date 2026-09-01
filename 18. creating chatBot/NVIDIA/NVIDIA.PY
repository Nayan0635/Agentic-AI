from openai import OpenAI 
from dotenv import load_dotenv
import os 

load_dotenv()



client = OpenAI(
    base_url = "https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_KEY")
)

while True:
    user_input = input("enter prompt :")
    if user_input.lower()=='exit':
        print("Bot : Cya! Have a great day!")
        exit(0)
    #Connect to llm.
    responses = client.chat.completions.create(
        
        model="meta/llama-3.3-70b-instruct",
        temperature=1,
        # max_tokens=1000,
        messages=[
            {
                "role":"system","content":'''
                 -You are an AI expert Customized ChatBot who will only answer about EjobIndia like courses , fees , placements etc.
                 -Your Name is "EjobBot max"
                 -Apart from EjobIndia related Please reply "I can only assist with Ejobindia related queries".
                 '''
            },
            {
                "role":"user","content":user_input
            }
        ]
    )
    msg = responses.choices[0].message.content
    print("Bot Reply :",msg)
