from google import genai
# from google.genai import types
import streamlit as st
from pypdf import PdfReader
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("gemini_key")
)
st.title("Renewable Energy")
# Read PDF
reader = PdfReader("./renewable_energy.pdf")
pdf_content = ""

for page in reader.pages:
    pdf_content += page.extract_text()

user_input = st.text_input("Ask something about Renewable_Energy:")

if st.button("Ask"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=f"""
                You are a PDF Summarizer AI.
                You can only answer from the provided PDF context.
                If the answer is not present in the PDF, reply:
                "I don't know anything about that."
                PDF Content:{pdf_content}
                User Question:{user_input}
                Answer only from the given PDF content."""
        )
        st.subheader("Agent: ")
        st.write(response.text)