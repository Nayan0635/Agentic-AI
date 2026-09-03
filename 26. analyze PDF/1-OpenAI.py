from openai import OpenAI
from pypdf import PdfReader
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key = os.getenv("openai_key"))

reader = PdfReader("./ejobIndia.pdf")
pdf_content = ""

for page in reader.pages:
    pdf_content += page.extract_text()

while True:
    user_input = input("Agent: ask about EjobIndia? ")
    if user_input.lower() == "exit":
        print("Agent: Cya!")
        exit(0)
    
    responses = client.chat.completions.create(
        model = "gpt-4.1-mini",
        messages = [
            {
                "role" : "system",
                "content" : '''
                -You are a PDF Summarizer AI
                -You can only answer from provided PDF context
                -Apart from that Please Reply I dont Know anything.
                '''
            },
            {
                "role" : "user",
                "content" : f'''
                -PDF Content:{pdf_content}
                -User Question :{user_input}
                -Answer only from Given PDF Content
                '''
            }
        ]
    )
    
    message = responses.choices[0].message.content
    print("Agent: ", message)