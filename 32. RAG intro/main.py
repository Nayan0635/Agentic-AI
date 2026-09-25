'''normal Python/text retrieval → user's query may not appear exactly in the document → beacuse Exact/keyword search → No Result
user must guess keywords → poor experience → semantic/vector search + RAG → user can ask naturally.'''


from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("openai_key")
)
#Static Data Source for AI Knowledge
documents =[
    "Python is a General Purpose Programming Language",
    "DJango is a Python Framework",
    "Node.js is a server runtime environment",
    "Node.js is asynchronous and single threaded",
    "React based on SPA or Single Page Application",
    "Learning React is Super easy",
    "PHP is Open Source",
    "PHP is used as a web technology",
    "Laravel is a MVC Framework of PHP"
]
#print(documents)
#print(len(documents))

#Retreval part
def retrieve(query:str):
    query = query.lower()
    for doc in documents:
        if query in doc.lower().split():
            return doc
    return "No such information found"

#ChatLoop
while True:
    user_input = input("You:")
    if user_input.lower()=='exit':
        print("Agent : Bye Bye")
        exit(0)
    context = retrieve(user_input)
    print("found context by Rag :",context)
    #Connecting to llm
    responses = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{
            "role":"user",
            "content":f'''
                -Context :{context}
                -Question: {user_input}
                -Please use above context to answer only
            '''}
        ]
    )
    msg = responses.choices[0].message.content
    print("Agent :",msg)