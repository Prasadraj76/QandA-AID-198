import asyncio
import os
import shutil

import streamlit as st
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from chunks import get_text_chunks
from embeddings import get_vector_store
from llm import get_conversational_chain
from load_data import load_webpage_as_document

load_dotenv()

# Ensure async loop exists
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())


def user_input(user_query):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    db = Chroma(persist_directory="chroma_db", embedding_function=embeddings)
    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 10})
    chain = get_conversational_chain(retriever)

    result = chain.invoke({"input": user_query})
    answer = result.get("answer", result.get("result", "No answer found."))

    st.write("### 📘 Answer:")
    st.success(answer)

    source_docs = result.get("context", [])
    if source_docs:
        with st.expander("Show retrieved context"):
            for i, doc in enumerate(source_docs):
                st.markdown(f"**Chunk {i+1}:**")
                st.code(doc.page_content[:500])
    else:
        st.info("No source documents returned.")


def main():
    st.set_page_config("Web Data Chat")
    st.title("💬 Chat with Any Webpage")

    user_question = st.text_input("🔍 Ask a question about the webpage")
    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("🌐 Web URL Loader")
        url = st.text_input("Paste the webpage URL")
        if st.button("🚀 Load & Process"):
            if not url.startswith("http"):
                st.error("Please enter a valid URL starting with http or https.")
                return
            with st.spinner("Loading and processing content..."):
                try:
                    raw_docs = load_webpage_as_document(url)
                    st.success(f"✅ Prview of Loaded document(s)")
                    st.code(raw_docs[0].page_content[:500])

                    chunks = get_text_chunks(raw_docs)

                    # Optional: Remove if you want persistent storage
                    if os.path.exists("chroma_db"):
                        shutil.rmtree("chroma_db")

                    get_vector_store(chunks)
                    st.success("✅ FAISS (Chroma) vector store created!")

                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")


if __name__ == "__main__":
    main()
