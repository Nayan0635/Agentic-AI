from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from prompts.food_order import prompt

load_dotenv()

llm = ChatGoogleGenerativeAI(
    api_key = os.getenv("gemini_key"),
    model = "gemini-3.1-flash-lite",
    temperature = 1
)
print("Agent: I can help you order Food Online.")

while True:
    user_input = input("You:")
    if user_input.lower() == 'exit':
        print("Agent: Cya! take care")
        exit(0)
    
    parser = StrOutputParser()
    chain = prompt | llm | parser
    responses = chain.invoke({"question" : user_input})
    print("Agent : ",responses)