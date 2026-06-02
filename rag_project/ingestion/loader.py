"""
Document loading module for RAG system
"""

from langchain_community.document_loaders import PyPDFLoader
from config.settings import PDF_PATH


def load_documents(pdf_path: str = PDF_PATH):
    """
    Load documents from PDF file

    Args:
        pdf_path: Path to PDF file

    Returns:
        List of Document objects
    """
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    return documents
