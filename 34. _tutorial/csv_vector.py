import pandas as pd
from google import genai
from dotenv import load_dotenv
import os
import chromadb
load_dotenv()
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
print("Gemini connected")
csv_file = "./documents/data.csv"
df = pd.read_csv(csv_file)
csv_data = df.to_string(index=False)
print("CSV loaded")
chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)
collection = chroma_client.get_or_create_collection(
    name="csv_documents"
)
response = client.models.embed_content(
    model="gemini-embedding-001",
    contents=csv_data
)
embedding = response.embeddings[0].values
collection.add(
    ids=["csv1"],
    embeddings=[embedding],
    documents=[csv_data]
)
print("CSV vector done")