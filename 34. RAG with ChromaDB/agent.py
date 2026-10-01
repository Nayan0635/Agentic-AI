from openai import OpenAI
from dotenv import load_dotenv
import os
import chromadb

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
#Connect to ChromaDB
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_collection(name="txt_doc")
print("Collection loaded")

#ChatLoop
while True:
    user_input = input("Ask About Ejobindia only ?")
    if user_input.lower()=='exit':
        print("Agent : Bye Bye")
        break
    if not user_input.strip():# FIXED: handle empty input gracefully.
        continue

    responses = client.embeddings.create(
        model="text-embedding-3-small",
        input=user_input
    )
    query_embedding = responses.data[0].embedding
    #Searching from ChromaDB
    result=collection.query(
        query_embeddings=[query_embedding],
        n_results=2
    )
    #Get the relavant documents
    docs = result.get('documents', [[]])[0] #oops?
    context = "\n".join(docs) if docs else "No relevant context found." # guard against empty results to avoid crashing on join.
    # print("Rag Context :",context)

    responses= client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role":"system",
                "content":'''
                    You are an assistant that answers ONLY from the provided context. 
                    If the answer is not in the context, reply exactly: 'I don't know'.
            '''},
            {
                "role":"user",
                "content":f'''
                -Context :{context}
                -Question:{user_input}
            '''}
        ]
    )
    msg = responses.choices[0].message.content
    print("Agent Final Reply :",msg)