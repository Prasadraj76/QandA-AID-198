from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Web Chat RAG API")
@app.get("/")
def root():
    return {"message": "FastAPI app is running"}

app.include_router(router)
