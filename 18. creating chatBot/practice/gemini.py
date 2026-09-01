from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key= os.getenv("key"))

while True:
    _input = input("You:")
    if _input.lower() == 'exit':
        print("Cya Have a great day!!")
        exit(0)
    
    response = client.model.generate_content(
        model = "gemini-3.1-flash-lite",#model name
        contents = _input,
        config = {
            "system_instruction" : '''
            -you are a dsa teacher
            -for every question you describe in details how to approach the problem
            -provide 3 solution to every question brute, better and optimal
            -after writting one solution you point out what can be improved and then write the next version
            '''
        }
    )
    msg = response.text
    print(msg)