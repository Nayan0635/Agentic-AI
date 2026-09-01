from openai import OpenAI
from dotenv import load_dotenv
import json
import os

from tool import tools
from functions import *

load_dotenv()
client = OpenAI(api_key=os.getenv("openai_key"))

while True:
    prompt = input("You: ")

    if prompt.lower() == "exit":
        print("Cya! Have a good day.")
        exit(0)

    responses = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0,
        messages=[{
            "role": "user",
            "content": f"""
            You are a student database agent.
            You can only:
            1. Add a student along with their course and enrollment.
            2. Show all students with their course and enrollment date.
            If the request is unrelated to these tasks, say:
            "Sorry, I can't help with that."
            Prompt: {prompt}
            """
            }],
        tools=tools
    )

    msg = responses.choices[0].message

    if msg.tool_calls:
        tool_name = msg.tool_calls[0].function.name
        tool_args = json.loads(
            msg.tool_calls[0].function.arguments
        )
        if tool_name == "addNew":
            answer = addNew(
                tool_args["name"],
                tool_args["email"],
                tool_args["address"],
                tool_args["course"]
            )
        elif tool_name == "showALL":
            answer = showALL()

        print("I'm using:", tool_name)
        print("Agent:", answer)
    else:
        print("Agent: Sorry, I can't help with that.")