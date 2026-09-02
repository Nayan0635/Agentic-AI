from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate 
from function import sendMail
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(
    api_key = os.getenv("gemini_key"),
    model = "gemini-3.6-flash"
)

llm = llm.bind_tools([sendMail])

while True:
    user_input = input("Agent: ")
    if user_input.lower() == 'exit':
        print("Agent: See ya!")
        exit(0)
    instructions = PromptTemplate(
        template = '''
        Please modify the body of the email intelligently.

        Rules:
        - Make the message professional and polite.
        - Correct grammar and spelling.
        - Keep the message short and meaningful.
        - Do not change the original intention.
        - Then send the email using the sendMail tool.
        user's request: {user_input}''',
        input_variables = ["user_input"]
     )
    
    myMessage = instructions.invoke({"user_input": user_input})
    responses = llm.invoke(myMessage)
    
    if responses.tool_calls:
        tool_name = responses.tool_calls[0]['name']
        tool_args = responses.tool_calls[0]['args']
        
        if tool_name == "sendMail":
            answer = sendMail.invoke(tool_args)
            print("Agent:", answer)
        else:
            print("I can't help with that.")