import os

from dotenv import load_dotenv

load_dotenv()
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings


def get_vector_store(text_chunks):
    """
    Embed the text chunks using Google Generative AI and store them in Chroma vector DB.
    """
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
    )
    vector_store = Chroma.from_documents(
        documents=text_chunks, embedding=embeddings, persist_directory="./chroma_db"
    )
    print("Vector DB created and persisted.")
    return vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 10})
