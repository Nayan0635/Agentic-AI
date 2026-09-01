from openai import OpenAI
from dotenv import load_dotenv
from pypdf import PdfReader
import os

load_dotenv()

#Connect to OpenAI LLM.
client = OpenAI(api_key=os.getenv("openai_key"))
print("Connected to OpenAI")

#Reading from specified pdf.
reader = PdfReader("./EjobIndia.pdf")
pdf_content:str='' #empty str

for page in reader.pages:
   pdf_content+= page.extract_text()

# print(pdf_content)

#ChatLoop
while True:
   user_input = input("Ask something about EjobIndia?")
   if user_input.lower()=='exit':
      print("Agent: Bye Bye")
      exit(0)
   #Sending pdf content to OpenAI for Ananlysis
   responses = client.chat.completions.create(
      model="gpt-4.1-mini",
      messages=[
         {
            "role":"system",
            "content":'''
             -You are a PDF Summarizer AI
             -You can only answer from provided PDF context
             -Apart from that Please Reply I dont Know anything.
             '''
         },
         {
            "role":"user",
            "content":f'''
             -PDF Content:{pdf_content}
             -User Question :{user_input}
             -Answer only from Given PDF Content 
            '''
         }
      ]
   )

   message = responses.choices[0].message.content
   print("Agent Final Reply:",message)