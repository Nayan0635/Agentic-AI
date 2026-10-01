#loading the required libraries
from openai import OpenAI
from dotenv import load_dotenv
import os
#importing chromadb vector database
import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()
#Connecting to openAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
print("OpenAI connected")

#Create Chromadb vector database
chroma_client = chromadb.PersistentClient(path="./chroma_db")
#Create a collection where we need to store the vector data.
collection = chroma_client.get_or_create_collection(name="company_documents")

source = "data.txt"
with open(f"./documents/{source}", "r", encoding="utf-8") as file:
    text = file.read()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = text_splitter.split_text(text)
if not chunks:
    raise ValueError("The TXT file is empty; no chunks were created.")

responses = client.embeddings.create(
    model="text-embedding-3-small",
    input=chunks
)
embeddings = [item.embedding for item in responses.data]

collection.delete(where={"source": source})
collection.delete(ids=["doc1"])
collection.upsert(
    ids=[f"doc_{i}" for i in range(len(chunks))],
    embeddings=embeddings,
    documents=chunks,
    metadatas=[{"source": source, "chunk_index": i} for i in range(len(chunks))]
)
print("ChromaDB database created successfully")

    
