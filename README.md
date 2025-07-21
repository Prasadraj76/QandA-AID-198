🧠 QANDA: Chat with Any Webpage Using LLMs
This project enables users to load any webpage, convert its content into embeddings, and chat with it using LLMs. You can interact via a Streamlit interface or through a FastAPI backend.

🚀 Features
🌐 Load and parse webpage content (e.g., Gutenberg books)

🧩 Chunk text for embedding

🔍 Store in Chroma vector DB

🤖 Ask questions with RAG (Retrieval-Augmented Generation) using Google Gemini 1.5 Flash

🖥️ Dual Interface:

app_streamlit.py for interactive Streamlit app

FastAPI (main.py + routes.py) for backend service

📂 Project Structure
bash
Copy
Edit
QANDA/
│
├── app/
│   ├── __init__.py
│   ├── main.py            # FastAPI entry point
│   ├── routes.py          # API endpoints
│   ├── pipeline.py        # Core logic (load, chunk, embed, query)
│
├── chroma_db/             # Chroma vector DB persistence
├── app_streamlit.py       # Streamlit app
├── chunks.py              # Text chunking logic (modular)
├── embeddings.py          # Embedding logic (Google Generative AI)
├── llm.py                 # Gemini LLM prompt and chain
├── load_data.py           # Web loader module
├── prompts.py             # Prompt templates
├── notebook.ipynb         # (Optional) Development notebook
├── requirements.txt       # Python dependencies
├── .env                   # Google API keys
├── .gitignore
└── README.md
🧪 Installation
1. Clone the repo
bash
Copy
Edit
git clone https://github.com/your-username/QANDA.git
cd QANDA
2. Set up a virtual environment
bash
Copy
Edit
python -m venv QandAvenv
# Activate it:
# On Windows:
QandAvenv\Scripts\activate
# On macOS/Linux:
source QandAvenv/bin/activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
🔐 Environment Setup
Create a .env file with your Google Generative AI API Key:

ini
Copy
Edit
GOOGLE_API_KEY=your_google_genai_key_here
🖥️ Streamlit UI
Run the Streamlit interface:

bash
Copy
Edit
streamlit run app_streamlit.py
Usage
Enter a webpage URL (e.g., a Project Gutenberg .txt link)

Ask natural language questions about the content

View accurate, context-based answers

⚙️ FastAPI Backend
Run the server
bash
Copy
Edit
uvicorn app.main:app --reload
Endpoints
POST /load
Loads and indexes the webpage content:

json
Copy
Edit
{
  "url": "https://www.gutenberg.org/cache/epub/100/pg100.txt"
}
POST /ask
Ask questions about the loaded content:

json
Copy
Edit
{
  "question": "Who is Hamlet?"
}
Returns:

json
Copy
Edit
{
  "answer": "Hamlet is the Prince of Denmark...",
  "sources": ["<snippet from the text>"]
}
📦 Dependencies
streamlit

fastapi

uvicorn

langchain

langchain_chroma

langchain_google_genai

chromadb

python-dotenv

pydantic

📌 Tips
Ensure your Google API key has access to both embedding-001 and gemini-1.5-flash.

Webpage parsing is handled by langchain_community.document_loaders.WebBaseLoader.

📈 Roadmap
✅ Dual interface (Streamlit + FastAPI)

🚧 Support PDFs, YouTube transcripts

🚀 Deployment via Hugging Face Spaces or Render

🧑‍💻 Author
Prasadraj — Built with ❤️ using LangChain + Gemini