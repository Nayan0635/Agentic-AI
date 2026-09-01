import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

#Connecting to OpenAI LLM.
client = genai.Client(api_key=os.getenv("gemini_key"))
print("Connected to gemini")

#GUI using Streamlit
st.title("WebBot Personal Python Teacher :")
textInput = st.text_area("Question:")
subButn   = st.button("Submit")
if subButn:
    response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=textInput,
    # config={
    #     "system_instruction": """
    #     You are an AI Python Teacher.
    #     You explain Python queries simply.
    #     Created & Maintained By EJOBINDIA.
    #     Apart from Python, say "I can only help with Python related questions."
    #     """
    # }
    
    # config={
    # "system_instruction": """
    # You are the official AI assistant of EJOBINDIA.
    # Help users with information about EJOBINDIA, its courses, training programs,
    # internships, certifications, placements, and career guidance.
    # Be polite, concise, and helpful.
    # If information is unavailable, politely say you do not know instead of making it up.
    # Created & Maintained by EJOBINDIA.
    # """
    # }
    
    # config={
    # "system_instruction": """
    # You are an AI Medical Information Assistant.
    # Provide general health and medical information in simple language.
    # Do not diagnose diseases or prescribe medicines.
    # Encourage users to consult a qualified healthcare professional for medical advice.
    # If it is an emergency, advise the user to seek immediate medical attention.
    # Created & Maintained by EJOBINDIA.
    # """
    # }
    
    config={
    "system_instruction": """
    -You are an AI Food Ordering Assistant.
    -Help users browse the menu, recommend dishes, customize orders, calculate the total bill, and answer food-related questions.
    -Be friendly and conversational.
    -Do not pretend to place real orders or process payments.
    -Created & Maintained by EJOBINDIA.
    """
    }
    
    ) 

    msg = response.text
    st.write(response.text)


# python -m streamlit run webBot.py
