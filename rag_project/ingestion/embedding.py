"""
Embedding module for RAG system

WHY?
- Avoid recomputing embeddings repeatedly
- In production: Redis, Disk cache, Vector cache
- Here we use persistent Chroma storage
"""

from langchain_huggingface import HuggingFaceEmbeddings
from config.settings import EMBEDDING_MODEL_NAME


def get_embedding_model(model_name: str = EMBEDDING_MODEL_NAME):
    """
    Initialize and return embedding model

    Args:
        model_name: Name of the embedding model

    Returns:
        HuggingFaceEmbeddings instance
    """
    embedding_model = HuggingFaceEmbeddings(model_name=model_name)
    return embedding_model
