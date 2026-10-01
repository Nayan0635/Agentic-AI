from openai import OpenAI
from dotenv import load_dotenv
import os
import chromadb

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Connect to ChromaDB
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_collection(name="company_documents")
print("Collection loaded")

# Chat loop
while True:
    user_input = input("Ask About Ejobindia only ?")
    if user_input.strip().lower() == "exit":
        print("Agent : Bye Bye")
        break
    if not user_input.strip():
        continue

    responses = client.embeddings.create(
        model="text-embedding-3-small",
        input=user_input
    )
    query_embedding = responses.data[0].embedding

    # Search ChromaDB for the most relevant chunks.
    result = collection.query(
        query_embeddings=[query_embedding],
        n_results=4
    )
    documents = result.get("documents") or [[]]
    context = "\n".join(documents[0]) if documents and documents[0] else "No relevant context found."
    print("Rag Context :", context)

    responses = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Answer only from the provided context. If the answer is not "
                    "in the context, reply exactly: I don't know."
                )
            },
            {
                "role": "user",
                "content": f"Context: {context}\nQuestion: {user_input}"
            }
        ]
    )
    msg = responses.choices[0].message.content
    print("Agent Final Reply :", msg)