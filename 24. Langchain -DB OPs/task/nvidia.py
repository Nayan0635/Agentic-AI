from langchain_nvidia_ai_endpoints import ChatNVIDIA
import os
# import sys
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dotenv import load_dotenv
from functions import *

load_dotenv()
#connect to llm.
llm = ChatNVIDIA(
    api_key=os.getenv("nvidia_key"),
    model="meta/muse-glimmer-30b",
    temperature=1,
    top_p=0.95,
    max_completion_tokens=8192
)
print("NVIDIA connected")
#bidning the llm with specified tools
llm = llm.bind_tools([addNew,showOne,showAll, delete, update])

tools_by_name:dict={
  "addNew":addNew,
  "showAll":showAll,
  "showOne":showOne,
  "update":update,
  "delete":delete
}

#Chat Loop :
while True:
    user_input = input("You :")
    if user_input.lower()=='exit' or user_input.lower()=='quit':
        print("Agent : Cya! Have a great day!")
        break
    #connect to llm.
    responses = llm.invoke(f'''
    Prompt :{user_input}
    ''')
    #Now we need to check whether ai is using the tools or not.
    if responses.tool_calls:
        tool_name = responses.tool_calls[0]['name']
        tool_args = responses.tool_calls[0]['args']
        
        print("Agent is using tool :",tool_name)
        #Now executing the specific tools
        result = tools_by_name.get(tool_name).invoke(tool_args)
        print("AI Reply :",result)
    else:
        print("Agent : Sorry I cann't help with that")

