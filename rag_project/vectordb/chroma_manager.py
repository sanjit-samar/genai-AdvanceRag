"""
Vector database manager using Chroma

WHY?
- Chroma provides persistent storage for embeddings
- Persistent storage avoids recomputing embeddings
- Efficient retrieval with similarity search
"""

from langchain_community.vectorstores import Chroma
import os
from config.settings import PERSIST_DIRECTORY


def create_or_load_vector_store(
    documents, embedding_model, persist_dir: str = PERSIST_DIRECTORY
):
    """
    Create or load vector store from persistent storage

    Args:
        documents: List of Document objects with embeddings
        embedding_model: Embedding model instance
        persist_dir: Directory to persist vector store

    Returns:
        Chroma vector store instance
    """
    if not os.path.exists(persist_dir):
        # Create new vector store
        vector_store = Chroma.from_documents(
            documents=documents,
            embedding=embedding_model,
            persist_directory=persist_dir,
        )
    else:
        # Load existing vector store
        vector_store = Chroma(
            persist_directory=persist_dir, embedding_function=embedding_model
        )

    return vector_store


def get_vector_retriever(
    vector_store,
    search_type: str = "mmr",
    k: int = 4,
    fetch_k: int = 10,
    lambda_mult: float = 0.7,
):
    """
    Get vector retriever from vector store

    Args:
        vector_store: Chroma vector store instance
        search_type: Type of search (e.g., "mmr", "similarity")
        k: Number of documents to retrieve
        fetch_k: Number of documents to fetch before filtering
        lambda_mult: Diversity parameter for MMR

    Returns:
        Vector retriever instance
    """
    retriever = vector_store.as_retriever(
        search_type=search_type,
        search_kwargs={"k": k, "fetch_k": fetch_k, "lambda_mult": lambda_mult},
    )
    return retriever
