# 🧠 QANDA: Chat with Any Webpage Using LLMs

This project enables users to **load any webpage**, convert its content into **embeddings**, and chat with it using **LLMs**. You can interact via a **Streamlit interface** or through a **FastAPI backend**.

---

## 🚀 Features

* 🌐 Load and parse webpage content (e.g., Gutenberg books)
* 🧹 Chunk text for embedding
* 🔍 Store in **Chroma vector DB**
* 🤖 Ask questions with RAG using **Google Gemini 1.5 Flash**
* 🖥️ Dual Interface:

  * `app_streamlit.py` — Streamlit App
  * FastAPI (`main.py`, `routes.py`) — Backend API

---

## 📂 Project Structure

```
QANDA/
│
├── app/
│   ├── __init__.py
│   ├── main.py            # FastAPI entry point
│   ├── routes.py          # API endpoints
│   ├── pipeline.py        # Core logic (load, chunk, embed, query)
│
├── chroma_db/             # Chroma vector DB
├── app_streamlit.py       # Streamlit app
├── chunks.py              # Text chunking logic
├── embeddings.py          # Embedding logic
├── llm.py                 # LLM prompt + chain
├── load_data.py           # Web loader
├── prompts.py             # Prompt templates
├── .env                   # API Keys
├── requirements.txt       # Dependencies
├── README.md              # This file
```

---

## 🧪 Installation

### 1. Clone the repo

```bash
git clone https://github.com/Prasadraj76/QandA-AID-198.git
cd QandA-AID-198
```

### 2. Set up a virtual environment

#### On Windows:

```bash
python -m venv QandAvenv
QandAvenv\Scripts\activate
```

#### On macOS/Linux:

```bash
python3 -m venv QandAvenv
source QandAvenv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Setup

Create a `.env` file:

```
GOOGLE_API_KEY=your_google_genai_key
```

Make sure your API key has access to:

* `models/embedding-001`
* `models/gemini-1.5-flash`

---

## 🖥️ Using the Streamlit App

```bash
streamlit run app_streamlit.py
```

1. Enter a webpage URL (e.g., a Gutenberg `.txt` file)
2. Ask a natural language question
3. Get context-aware answers

---

## ⚙️ FastAPI Backend

### Start the API Server

```bash
uvicorn app.main:app --reload
```

### Endpoints

#### `POST /load`

Load and index a webpage:

```json
{
  "url": "https://www.gutenberg.org/cache/epub/100/pg100.txt"
}
```

#### `POST /ask`

Ask a question about the indexed content:

```json
{
  "question": "Who is Hamlet?"
}
```

#### Sample Response

```json
{
  "answer": "Hamlet is the Prince of Denmark...",
  "sources": ["sources"]
}
```

---

## 📦 Dependencies

* `streamlit`
* `fastapi`
* `uvicorn`
* `langchain`
* `langchain_chroma`
* `langchain_google_genai`
* `chromadb`
* `python-dotenv`
* `pydantic`

---

## 📌 Notes

* Ensure your Google API key has access to both `embedding-001` and `gemini-1.5-flash`.
* Webpage parsing is handled by:
  `langchain_community.document_loaders.WebBaseLoader`

---

## 🧱 Roadmap

* ✅ Dual mode: Streamlit & FastAPI
* 📄 Add PDF, YouTube support
* ☁️ Deploy to HuggingFace or Render
* 📌 Add query history tracking

---

## 👨‍💻 Author

**Prasadraj** — Built with ❤️ using LangChain + Gemini
