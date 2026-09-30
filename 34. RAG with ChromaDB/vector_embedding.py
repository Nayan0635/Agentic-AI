from openai import OpenAI
from dotenv import load_dotenv
import os
import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="txt_doc")

with open("./documents/data.txt", "r", encoding="utf-8") as file:
    text = file.read()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = text_splitter.split_text(text)

responses = client.embeddings.create(
    model="text-embedding-3-small",
    input=chunks
)
embeddings = [item.embedding for item in responses.data]

collection.add(
    ids=[f"doc_{i}" for i in range(len(chunks))],
    embeddings=embeddings,
    documents=chunks,
    metadatas=[{"source": "data.txt", "chunk_index": i} for i in range(len(chunks))]
)

print("ChromaDB created successfully")