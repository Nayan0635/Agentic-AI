from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from function import sendMail
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    api_key= os.getenv("openai_key"),
    model= "gpt-4.1-mini",
    temperature= 1
)

llm.bind_tools([sendMail])

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Agent: Cya! Have a good day!")
        exit(0)
    
    prompt = PromptTemplate(
        template="""
        Please modify the body of the email intelligently.

        Rules:
        - Make the message professional and polite.
        - Correct grammar and spelling.
        - Keep the message short and meaningful.
        - Do not change the original intention.
        - Then send the email using the sendMail tool.

        User's request:{user_input}""",
        input_variables= ["user_input"]
    )
    
    myMessage = prompt.invoke({"user_input": user_input})
    responses = llm.invoke(myMessage)
    
    if responses.tool_calls:
        tool_name = responses.tool_calls[0]['name']
        tool_args = responses.tool_calls[0]['args']
        
        if tool_name == "sendMail":
            result = sendMail.invoke(tool_args)
            print("Agent: ",result)
    else:
        print("Sorry I can't help with that.")