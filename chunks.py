from langchain.text_splitter import RecursiveCharacterTextSplitter


def get_text_chunks(docs):
    """This function uses the RecursiveCharacterTextSplitter to divide large documents into
    manageable pieces, preserving semantic meaning while respecting token/character limits
    for embedding and retrieval tasks."""
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    return splitter.split_documents(docs)
