from google import genai
from dotenv import load_dotenv
import os
import chromadb
from docx import Document
load_dotenv()
# Gemini
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
print("Gemini connected")
# Read DOCX
doc = Document("./documents/document.docx")
text = "\n".join(
    paragraph.text
    for paragraph in doc.paragraphs
    if paragraph.text.strip()
)
print("DOCX loaded")
# ChromaDB
chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)
collection = chroma_client.get_or_create_collection(
    name="docx_documents"
)
# Create Embedding
response = client.models.embed_content(
    model="gemini-embedding-001",
    contents=text
)
embedding = response.embeddings[0].values
# Store Vector
collection.add(
    ids=["docx1"],
    embeddings=[embedding],
    documents=[text]
)
print("DOCX vector stored successfully")