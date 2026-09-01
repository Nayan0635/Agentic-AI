from google import genai
from dotenv import load_dotenv
from pypdf import PdfReader
import os

load_dotenv()

# Connect to Gemini
client = genai.Client(
    api_key=os.getenv("gemini_key")
)
print("Connected to Gemini")

# Reading PDF from main folder
reader = PdfReader("./EjobIndia.pdf")

pdf_content: str = ""

for page in reader.pages:
    pdf_content += page.extract_text()

# ChatLoop
while True:
    user_input = input("Ask something about EjobIndia? ")

    if user_input.lower() == "exit":
        print("Agent: Bye Bye")
        exit(0)

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

    print("Agent Final Reply:", response.text)