from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from functions import *

load_dotenv()
# connect to llm.
llm = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    model="gpt-4o-mini",
    temperature=0
)
print("OpenAI connected")
# binding the llm with specified tools
llm = llm.bind_tools([addNew, findOne, showAll, delete, update])

tools_by_name: dict = {
    "showAll": showAll,
    "findOne": findOne,
    "addNew": addNew,
    "update": update,
    "delete": delete
}

# Chat Loop :
while True:
    user_input = input("You :")
    if user_input.lower() == 'exit' or user_input.lower() == 'quit':
        print("Agent : Bye Bye")
        break
    # connect to llm.
    responses = llm.invoke(f'''
    Prompt :{user_input}
    ''')
    # Now we need to check whether ai is using the tools or not.
    if responses.tool_calls:
        tool_name = responses.tool_calls[0]['name']
        tool_args = responses.tool_calls[0]['args']
        
        print("Agent is using tool :", tool_name)
        # Now executing the specific tools
        result = tools_by_name.get(tool_name).invoke(tool_args)
        print("AI Reply :", result)
    else:
        print("Agent :", responses.content)

