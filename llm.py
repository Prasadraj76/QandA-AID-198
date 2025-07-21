from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_google_genai import ChatGoogleGenerativeAI

from prompts import prompt_for_llm


def get_conversational_chain(retriever):
    """Builds a conversational Retrieval-Augmented Generation (RAG) chain using Gemini and a retriever."""
    model = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash", temperature=0.3)
    question_answer_chain = create_stuff_documents_chain(model, prompt_for_llm)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    return rag_chain
