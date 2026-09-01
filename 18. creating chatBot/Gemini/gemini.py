from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

#Connect to gemini
client = genai.Client(api_key=os.getenv("gemini_key"))
print("Connected to Gemini")


#ChatLoop
while True:
    user_input = input("enter prompt:")
    if user_input.lower()=='exit':
        print("Bot :Bye Bye")
        exit(0)
    #Connect to LLM i.e Gemini
    responses = client.models.generate_content(
        model="gemini-3.1-flash-lite", #RPM 15 RPD 500
        contents=user_input,
        config={
            "system_instruction":'''
            -you are math teacher can calculate problems and return result
            '''
        }
    )
    msg = responses.text
    print("Bot Reply :",msg)



# Task : Create a streamlit version of the same.
# Task 2: Create an customized ChatBot on EjobIndia using Gemini .
# Task 3: Create an Medical Informative ChatBot using Gemini.
# Task 4: Create a Food Order related chatBot using Gemini.