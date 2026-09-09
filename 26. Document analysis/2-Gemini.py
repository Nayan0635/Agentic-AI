from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from pypdf import PdfReader
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(
    api_key = os.getenv("gemini_key"),
    model = "gemini-3.6-flash"
)

# Reading PDF from main folder
reader = PdfReader("./machine_learning.pdf")
pdf_content: str = ""

for page in reader.pages:
    pdf_content += page.extract_text()

prompt = PromptTemplate(
    template = """
    You are a PDF Summarizer AI.
    You can only answer from the provided PDF context.
    If the answer is not present in the PDF, reply:
    "I don't know anything about that."
    PDF Content:{pdf_content}
    User Question:{user_input}
    Answer only from the given PDF content.""",
    input_variables= ["pdf_content", "user_input"]
)

# ChatLoop
while True:
    user_input = input("Agent: ask me about Machine Learning? ")

    if user_input.lower() == "exit":
        print("Agent: Bye Bye")
        exit(0)
    
    _prompt = prompt.invoke({
        "pdf_content" : pdf_content,
        "user_input" : user_input
    })
    
    responses = llm.invoke(_prompt)
    print("Agent: ", responses.content[0]['text'])
    
    