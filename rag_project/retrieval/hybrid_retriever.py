"""
Hybrid retrieval module for RAG system

WHY?
- Vector Search: Good for semantic meaning
- BM25: Good for exact keywords
- Hybrid retrieval combines both for better results
"""

from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever
from config.settings import (
    BM25_K,
    ENSEMBLE_WEIGHTS,
    VECTOR_SEARCH_TYPE,
    VECTOR_K,
    VECTOR_FETCH_K,
    VECTOR_LAMBDA_MULT,
)


def create_bm25_retriever(documents, k: int = BM25_K):
    """
    Create BM25 retriever for keyword-based search

    Args:
        documents: List of Document objects
        k: Number of documents to retrieve

    Returns:
        BM25Retriever instance
    """
    bm25_retriever = BM25Retriever.from_documents(documents)
    bm25_retriever.k = k
    return bm25_retriever


def create_hybrid_retriever(
    vector_retriever, bm25_retriever, weights: list = ENSEMBLE_WEIGHTS
):
    """
    Create hybrid retriever combining vector and BM25 search

    Args:
        vector_retriever: Vector retriever instance
        bm25_retriever: BM25 retriever instance
        weights: Weights for ensemble [bm25_weight, vector_weight]

    Returns:
        EnsembleRetriever instance
    """
    hybrid_retriever = EnsembleRetriever(
        retrievers=[bm25_retriever, vector_retriever], weights=weights
    )
    return hybrid_retriever
