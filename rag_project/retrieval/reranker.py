"""
Re-ranking module for RAG system

WHY?
- Retriever may return partially relevant chunks
- Re-ranker improves ranking quality
- CrossEncoder compares (query, chunk) and gives better relevance score
"""

from sentence_transformers import CrossEncoder
from config.settings import RERANKER_MODEL, TOP_K_RERANKED


def get_reranker(model_name: str = RERANKER_MODEL):
    """
    Initialize and return re-ranker model

    Args:
        model_name: Name of the cross-encoder model

    Returns:
        CrossEncoder instance
    """
    reranker = CrossEncoder(model_name)
    return reranker


def rerank_documents(query: str, documents, reranker, top_k: int = TOP_K_RERANKED):
    """
    Re-rank documents based on relevance to query

    Args:
        query: User query
        documents: List of Document objects to re-rank
        reranker: CrossEncoder instance
        top_k: Number of top documents to return

    Returns:
        List of re-ranked Document objects
    """
    # Create query-document pairs
    pairs = [[query, doc.page_content] for doc in documents]

    # Get relevance scores
    scores = reranker.predict(pairs)

    # Combine documents with scores
    scored_docs = list(zip(documents, scores))

    # Sort by score (descending)
    scored_docs = sorted(scored_docs, key=lambda x: x[1], reverse=True)

    # Extract top-k documents
    reranked_docs = [doc for doc, score in scored_docs[:top_k]]

    return reranked_docs
