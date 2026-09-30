from openai import OpenAI
from dotenv import load_dotenv
import os
import chromadb

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="txt_doc")
print("Collection loaded")

while True:
    user_input = input("Ask about the document: ")
    if user_input.lower() == "exit":
        print("Agent : Bye Bye")
        break
    if not user_input.strip():
        continue

    responses = client.embeddings.create(
        model="text-embedding-3-small",
        input=user_input
    )
    query_embedding = responses.data[0].embedding

    result = collection.query(
        query_embeddings=[query_embedding],
        n_results=3,
        include=["documents", "metadatas"]
    )

    docs = result.get("documents", [[]])[0]
    context = "\n".join(docs) if docs else "No relevant context found."

    responses = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": """
                    You are an assistant that answers ONLY from the provided context.
                    If the answer is not in the context, reply exactly: 'I don't know'.
                """
            },
            {
                "role": "user",
                "content": f"""
                    Context: {context}
                    Question: {user_input}
                    Please use the context to answer the question. Otherwise, say I don't know.
                """
            }
        ]
    )

    msg = responses.choices[0].message.content
    print("Agent Final Reply :", msg)

