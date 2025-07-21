import os
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from prompts import prompt_for_llm

load_dotenv()

def load_webpage_as_document(url):
    loader = WebBaseLoader(url)
    return loader.load()

def get_text_chunks(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    return splitter.split_documents(docs)

def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = Chroma.from_documents(
        documents=text_chunks,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )
    return vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 10})

def get_conversational_chain(retriever):
    model = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash", temperature=0.3)
    question_answer_chain = create_stuff_documents_chain(model, prompt_for_llm)
    return create_retrieval_chain(retriever, question_answer_chain)
