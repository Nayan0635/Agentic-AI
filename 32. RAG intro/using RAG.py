from openai import OpenAI
from dotenv import load_dotenv
import os
from sklearn.metrics.pairwise import cosine_similarity
load_dotenv()

client = OpenAI(
    api_key=os.getenv("openai_key")
)
print("Connected")

#Static Data Source
documents =[
    "Python is a general Purpose Programming Language",
    "Learning Python is quiet easy",
    "Django is a Python web framework",
    "React supports SPA or Single Page application",
    "Learning React is fun",
    "Node is a server side platform",
    "Node.js is asynchronous",
    "PHP is a web technology",
    "Laravel is a powerful framework of PHP"
]
document_vectors=[]
#We want to convert the entire doducments into vector embedding database.
for doc in documents:
    responses =client.embeddings.create(
        model="text-embedding-3-small",
        input=doc
    )
    document_vectors.append(
    {
        "text":doc,
        "vector":responses.data[0].embedding
    }
)

#print(document_vectors)
print("Vector Database created successfully")

#Retieve function 
def retrieve(query:str):
    query_responses = client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    )
    query_vector = query_responses.data[0].embedding
    
    scores =[] #emptly list
    for item in document_vectors:
        similarity = cosine_similarity(
            [query_vector],
            [item['vector']]
        )[0][0]
        #print(similarity)
        scores.append((similarity,item['text']))

    #we will make sore reverse to get top 2 records 
    scores.sort(reverse=True)
    #print(scores)
    top_docs =[
        text
        for score , text in scores[:2]
    ]
    return "\n".join(top_docs)


#Test retieve function 
#print(retrieve("What is Python?"))

#ChatLoop
while True:
    user_input = input("You:")
    if user_input.lower()=='exit':
        print("Agent: Bye Bye")
        exit(0)
    context = retrieve(user_input)    
    responses = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role":"user","content":f'''
            -Context:{context}
            -Question:{user_input}
            -Use the above context to reply answer
            -Apart from the context Please reply "I dont know"
'''}
        ]
    )
    msg = responses.choices[0].message.content
    #print("Rag Context send to the AI :",context)
    print("Agent Final Reply :",msg)

    #Basic Rag Pipe Line 
    #documents 
    # -> vector ->
    #  question ->vector 
    # => vector similarity search using consine similarity sarch 
    # -> find out relavant information 
    # -> send it to AI -> final answer