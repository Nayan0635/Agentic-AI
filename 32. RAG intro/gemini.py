from google import genai
from google.genai import types
import streamlit as st
from dotenv import load_dotenv
import os
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

client = genai.Client(
    api_key=os.getenv("gemini_key")
)
print("Connected")

# Static Data Source
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
def prepare_document(content):
    # For retrieval tasks, title can be left empty
    return f"title: none | text: {content}"

document_vectors = []

# Convert documents into vector embeddings
for doc in documents:
    # Add the task prefix
    formatted_content = prepare_document(doc)

    response = client.models.embed_content(
        model="gemini-embedding-001",  # Updated model name
        contents=formatted_content,
        config=types.EmbedContentConfig(
            output_dimensionality=768  # Recommended 768 dims, saves space with minimal quality loss
        )
    )

    document_vectors.append(
        {
            "text": doc,
            "vector": response.embeddings[0].values
        }
    )

print("Vector Database created successfully")


# Retrieve function
def retrieve(query: str):
    # Define the prefix format for query embedding (Gemini Embedding 2 specific)
    def prepare_query(q):
        # For question-answering retrieval tasks
        return f"task: question answering | query: {q}"

    formatted_query = prepare_query(query)

    query_response = client.models.embed_content(
        model="gemini-embedding-2",
        contents=formatted_query,
        config=types.EmbedContentConfig(
            output_dimensionality=768  # Must match the document embedding dimensions
        )
    )

    query_vector = query_response.embeddings[0].values

    scores = []

    for item in document_vectors:
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


# Streamlit UI
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