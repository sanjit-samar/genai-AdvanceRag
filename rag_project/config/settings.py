"""
Configuration and environment settings for RAG system
"""

from dotenv import load_dotenv
import os

load_dotenv()

# ============================================================
# ENVIRONMENT VARIABLES
# ============================================================

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# ============================================================
# EMBEDDING CONFIGURATION
# ============================================================

EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# ============================================================
# LLM CONFIGURATION
# ============================================================

LLM_MODEL = "mistral-small-2603"
LLM_TEMPERATURE = 0
LLM_STREAMING = True

# ============================================================
# VECTOR DATABASE CONFIGURATION
# ============================================================

PERSIST_DIRECTORY = "production_rag_db"

# ============================================================
# CHUNKING CONFIGURATION
# ============================================================

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# ============================================================
# RETRIEVAL CONFIGURATION
# ============================================================

# Vector retrieval parameters
VECTOR_SEARCH_TYPE = "mmr"
VECTOR_K = 4
VECTOR_FETCH_K = 10
VECTOR_LAMBDA_MULT = 0.7

# BM25 retrieval parameters
BM25_K = 4

# Ensemble weights (BM25, Vector)
ENSEMBLE_WEIGHTS = [0.4, 0.6]

# Re-ranking model
RERANKER_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"

# ============================================================
# RE-RANKING CONFIGURATION
# ============================================================

TOP_K_RERANKED = 4

# ============================================================
# MEMORY CONFIGURATION
# ============================================================

MEMORY_TYPE = "buffer"  # "buffer" or "summary"

# ============================================================
# DOCUMENT LOADING
# ============================================================

PDF_PATH = "sample.pdf"

# ============================================================
# SECURITY CONFIGURATION
# ============================================================

BLOCKED_PATTERNS = [
    "ignore previous instructions",
    "system prompt",
    "reveal hidden prompt",
    "bypass security",
]
