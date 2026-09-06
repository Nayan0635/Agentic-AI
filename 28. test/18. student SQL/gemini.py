from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os
from functions import *

load_dotenv()

llm = ChatGoogleGenerativeAI(
    api_key = os.getenv("gemini_key"),
    model = "gemini-3.1-flash-lite"
    
)

llm = llm.bind_tools([addNew,findOne,showAll, delete, update])

tools_by_name:dict={
  "showAll":showAll,
  "findOne":findOne,
  "addNew":addNew,
  "update":update,
  "delete":delete
}

while True:
    user_input = input("You :")
    if user_input.lower()=='exit':
        print("Agent : Cya")
        break
    #connect to llm.
    responses = llm.invoke(f'''
    Prompt :{user_input}
    ''')
    #Now we need to check whether ai is using the tools or not.
    if responses.tool_calls:
        tool_name = responses.tool_calls[0]['name']
        tool_args = responses.tool_calls[0]['args']
        
        print("Agent is using tool :", tool_name)
        # Now executing the specific tools
        result = tools_by_name.get(tool_name).invoke(tool_args)
        print("AI Reply :", result)
    else:
        print("Agent :", responses.content)

