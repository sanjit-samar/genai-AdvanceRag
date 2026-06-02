"""
Document chunking module for RAG system

WHY?
- Large documents cannot be embedded efficiently
- Chunking improves semantic retrieval accuracy
- Split documents into smaller chunks with overlap to preserve context continuity
"""

from langchain.text_splitter import RecursiveCharacterTextSplitter
from config.settings import CHUNK_SIZE, CHUNK_OVERLAP


def chunk_documents(
    documents, chunk_size: int = CHUNK_SIZE, chunk_overlap: int = CHUNK_OVERLAP
):
    """
    Split documents into chunks with overlap

    Args:
        documents: List of Document objects
        chunk_size: Size of each chunk
        chunk_overlap: Overlap between chunks

    Returns:
        List of chunked Document objects
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    split_docs = text_splitter.split_documents(documents)
    return split_docs


def add_metadata(split_docs, source_name: str = "sample.pdf"):
    """
    Add metadata to chunks for tracking and citations

    WHY?
    - Metadata helps source tracking, filtering, citations, and enterprise document control

    Args:
        split_docs: List of chunked Document objects
        source_name: Name of the source document

    Returns:
        List of Document objects with metadata
    """
    for idx, doc in enumerate(split_docs):
        doc.metadata["chunk_id"] = idx
        doc.metadata["source"] = source_name

    return split_docs
