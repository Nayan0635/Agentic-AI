import pandas as pd
from google import genai
from dotenv import load_dotenv
import os
import chromadb
load_dotenv()
# Gemini
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
print("Gemini connected")
# Read Excel
excel_file = "./documents/retail_sales.xlsx"
df = pd.read_excel(excel_file)
excel_data = df.to_string(index=False)
print("Excel loaded")
# ChromaDB
chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)
collection = chroma_client.get_or_create_collection(
    name="excel_documents"
)
# Create Embedding
response = client.models.embed_content(
    model="gemini-embedding-001",
    contents=excel_data
)
embedding = response.embeddings[0].values
# Store Vector
collection.add(
    ids=["excel1"],
    embeddings=[embedding],
    documents=[excel_data]
)
print("Excel vector stored successfully")