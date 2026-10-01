from openai import OpenAI
from dotenv import load_dotenv
import os
import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

chroma_client = chromadb.PersistentClient(path="./ChromaDB")
collection = chroma_client.get_or_create_collection(name="txt_doc")

#fetching from .txt file
with open("./documents/data.txt", "r") as file:
    text = file.read()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = text_splitter.split_text(text)
# print(f"Total chunks created: {len(chunks)}")

# Embed all chunks in one API call
responses = client.embeddings.create(
    model="text-embedding-3-small",
    input=chunks
)
embeddings = [d.embedding for d in responses.data]

collection.add(
    ids=[f"doc_{i}" for i in range(len(chunks))],
    embeddings=embeddings,
    documents=chunks,
    # optional but recommended: keep source metadata for traceability
    metadatas=[{"source": "data.txt", "chunk_index": i} for i in range(len(chunks))]
)
print("txt stored successfully")