from langchain_community.document_loaders import WebBaseLoader


def load_webpage_as_document(url):
    """Loads the content of a webpage and returns it as a LangChain Document object."""
    loader = WebBaseLoader(url)
    return loader.load()
