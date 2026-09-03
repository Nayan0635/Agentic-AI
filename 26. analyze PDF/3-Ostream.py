import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
from pypdf import PdfReader
import os

load_dotenv()

# Connect to OpenAI LLM
client = OpenAI(
    api_key=os.getenv("openai_key")
)
st.title("PDF Summarizer AI")
# Reading PDF
reader = PdfReader("./networking.pdf")
pdf_content = ""
for page in reader.pages:
    pdf_content += page.extract_text()
# User question
user_input = st.text_input("Ask me about Networking...")
# Submit button
if st.button("Ask"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        # Sending PDF content to OpenAI for analysis
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": """
                    You are a PDF Summarizer AI.
                    You can only answer from the provided PDF context.
                    If the answer is not available in the PDF,
                    reply: I don't know."""
                },
                {
                    "role": "user",
                    "content": f"""
                    PDF Content: {pdf_content}

                    User Question: {user_input}
                    Answer only from the given PDF content."""
                }
            ]
        )
        message = response.choices[0].message.content
        st.write("Agent:")
        st.write(message)