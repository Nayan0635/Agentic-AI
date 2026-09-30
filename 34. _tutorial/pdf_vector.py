from google import genai
from dotenv import load_dotenv
import os
import chromadb
from pypdf import PdfReader
load_dotenv()
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
print("Gemini connected")
pdf_file = "./documents/data.pdf"
reader = PdfReader(pdf_file)
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"
print("PDF loaded")
chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)
collection = chroma_client.get_or_create_collection(
    name="pdf_documents"
)
response = client.models.embed_content(
    model="gemini-embedding-001",
    contents=text
)
embedding = response.embeddings[0].values
collection.add(
    ids=["pdf1"],
    embeddings=[embedding],
    documents=[text]
)
print("PDF vector stored")