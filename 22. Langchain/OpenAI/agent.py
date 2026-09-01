from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from prompts.food_order import prompt
load_dotenv()

llm = ChatOpenAI(
    api_key = os.getenv("openai_key"),
    model = "gpt-4.1-mini",
    temperature = 1
)
print("OpenAI connecterd")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Agent: Cya! have a great day!")
        exit(0)
        
        chain = prompt | llm
        responses = chain.invoke({"question" : user_input})
        print("Agent: ", responses.text)
        

