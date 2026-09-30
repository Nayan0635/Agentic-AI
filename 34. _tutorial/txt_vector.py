#loading the required libraries
from openai import OpenAI
from dotenv import load_dotenv
import os
#importing chromadb vector database
import chromadb

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

text=""
#fetching from .txt file 
with open("./documents/data.txt","r+") as file:
    text = file.read()
    file.close()
print(text)

#Create the embeddings 
responses = client.embeddings.create(
    model="text-embedding-3-small",
    input=text
)
embedding = responses.data[0].embedding
print(embedding)
#We need to store these vectors inside the collection of the chromadb.
collection.add(
    ids=['doc1'],
    embeddings=[embedding],
    documents=[text]
)
print("ChromaDB database created successfully")

    
