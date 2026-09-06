import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import (
    calculator,
    sqlite_query,
    find_student_by_name,
    find_student_by_id,
    show_all_students,
    add_student,
    update_student,
    delete_student
)

# Load environment variables from .env
load_dotenv()

api_key = os.getenv("gemini_key")
if not api_key:
    raise ValueError("gemini_key not found in .env file. Please check your .env configuration.")

# Updated model name to gemini-3.6-flash
llm = ChatGoogleGenerativeAI(
    api_key=api_key,
    model="gemini-3.6-flash"
)

# List of available tools for the Agent
tools = [
    calculator,
    sqlite_query,
    find_student_by_name,
    find_student_by_id,
    show_all_students,
    add_student,
    update_student,
    delete_student
]

# Map tool names to tool functions
tools_by_name = {t.name: t for t in tools}

# Bind tools to Gemini LLM
llm_with_tools = llm.bind_tools(tools)

def run_agent(user_input: str):
    """Process user prompt, invoke appropriate tools, and display the result."""
    print(f"\nUser: {user_input}")
    
    # Invoke Gemini with tool-calling capabilities
    response = llm_with_tools.invoke(user_input)
    
    # Check if Gemini triggered any tool calls
    if response.tool_calls:
        for tool_call in response.tool_calls:
            tool_name = tool_call["name"]
            tool_args = tool_call["args"]
            print(f"[Agent] Calling Tool: '{tool_name}' with args: {tool_args}")
            
            tool_fn = tools_by_name.get(tool_name)
            if tool_fn:
                result = tool_fn.invoke(tool_args)
                print(f"[Tool Output]: {result}")
            else:
                print(f"[Error]: Tool '{tool_name}' not found.")
    else:
        print(f"Agent: {response.content}")

if __name__ == "__main__":
    print("=== LangChain + Gemini Agentic AI Application ===")
    print("Available tools: Calculator, SQLite Database Tools")
    print("Type 'exit' to quit.\n")
    
    while True:
        try:
            user_input = input("You: ")
            if user_input.strip().lower() in ["exit", "quit"]:
                print("Agent: Goodbye!")
                break
            if not user_input.strip():
                continue
            run_agent(user_input)
        except (KeyboardInterrupt, EOFError):
            print("\nAgent: Goodbye!")
            break
