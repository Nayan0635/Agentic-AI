from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from tools import sendMail
from langchain_core.prompts import PromptTemplate
load_dotenv()

#Connecting to LLM.
llm = ChatGoogleGenerativeAI(
    api_key=os.getenv("gemini_key"),
    model="gemini-3.0-flash",
    # temperature=1
)
print("Connected to Gemini")

llm = llm.bind_tools([sendMail])
#Chat Loop
while True:
    user_input = input("You:")
    if user_input.lower()=='exit':
        print("Agent : Bye Bye")
        exit(0)
    #Connected to llm.
    #create Prompt 
  # Create Prompt
    prompt = PromptTemplate(
        template="""
            Please modify the body of the email intelligently.

            Rules:
            - Make the message professional and polite.
            - Correct grammar and spelling.
            - Keep the message short and meaningful.
            - Do not change the original intention.
            - Then send the email using the sendMail tool.

            User's request:
            {user_input}
        """,
    input_variables=["user_input"]
)

    myMessages = prompt.invoke({"user_input":user_input})
    responses = llm.invoke(myMessages)
    if  responses.tool_calls:
        tool_name = responses.tool_calls[0]['name']
        tool_args = responses.tool_calls[0]['args']
        if tool_name == "sendMail":
            result = sendMail.invoke(tool_args)
            print("Agent Reply :",result)
    else:
        print("Sorry I can't help with that.")