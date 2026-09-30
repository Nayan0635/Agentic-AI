from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

embeddings = OpenAIEmbeddings(
    api_key = os.getenv("OPENAI_API_KEY"),
    model = "text-embedding-3-small"
)
