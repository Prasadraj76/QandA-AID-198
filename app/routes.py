from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from .pipeline import load_webpage_as_document, get_text_chunks, get_vector_store, get_conversational_chain

router = APIRouter()

class URLRequest(BaseModel):
    url: str

class QueryRequest(BaseModel):
    question: str

retriever = None
rag_chain = None

@router.post("/load")
def load_and_process(request: URLRequest):
    import asyncio
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        asyncio.set_event_loop(asyncio.new_event_loop())

    global retriever, rag_chain
    try:
        raw_docs = load_webpage_as_document(request.url)
        chunks = get_text_chunks(raw_docs)
        retriever = get_vector_store(chunks)
        rag_chain = get_conversational_chain(retriever)
        return {"message": "Document loaded and vector store created successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/ask")
def ask_question(request: QueryRequest):
    if not rag_chain:
        raise HTTPException(status_code=400, detail="Vector store not loaded.")
    result = rag_chain.invoke({"input": request.question})
    return {
        "answer": result.get("answer", "No answer found."),
        "sources": [doc.page_content[:500] for doc in result.get("source_documents", [])]
    }
