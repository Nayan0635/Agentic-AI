from google import genai
from google.genai import types

from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client(
    api_key=os.getenv("gemini_key")
)

documents = [
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
# Define the prefix format for document embedding (Gemini Embedding 2 specific)
def retrieve(content):
    # For retrieval tasks, title can be left empty
    return f"title: none | text: {content}"
embedded_doc = []
# Convert documents into vector embeddings
for doc in documents:
    # Add the task prefix
    formatted_content = retrieve(doc)
    response = client.models.embed_content(
        model="gemini-embedding-001", #-> notice
        contents=formatted_content,
        config=types.EmbedContentConfig(
            output_dimensionality=768  # Recommended 768 dims, saves space with minimal quality loss
        )
    )
    embedded_doc.append(
        {
            "text": doc,
            "vector": response.embeddings[0].values
        }
    )
print("Embedded Document generated.")


from sklearn.metrics.pairwise import cosine_similarity

def retrieve(query: str):
    # Define the prefix format for query embedding (Gemini Embedding 2 specific)
    def prepare_query(q):
        # For question-answering retrieval tasks
        return f"task: question answering | query: {q}"
    formatted_query = prepare_query(query)
    query_response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=formatted_query,
        config=types.EmbedContentConfig(
            output_dimensionality=768  # Must match the document embedding dimensions
        )
    )
    query_vector = query_response.embeddings[0].values
    scores = []
    for item in embedded_doc:
        similarity = cosine_similarity(
            [query_vector],
            [item["vector"]]
        )[0][0]
        scores.append((similarity, item["text"]))
    scores.sort(reverse=True)
    top_docs = [
        text
        for score, text in scores[:2]
    ]
    return "\n".join(top_docs)

import streamlit as st
st.title("Gemini RAG Agent")
user_input = st.text_input("Ask something:")
if user_input:
    context = retrieve(user_input)
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=f"""
        - Context: {context}
        - Question: {user_input}
        - Use the above context to reply answer.
        - Apart from the context, please reply "I don't know".
        """
    )
    st.write(response.text)