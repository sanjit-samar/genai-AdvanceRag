"""
Main RAG Application

Production-Ready RAG Pipeline with:
- Document Chunking
- Metadata Support
- Source Citations
- Conversation Memory
- Query Rewriting
- Re-ranking
- Better Prompt Engineering
- Structured Retrieval Chain
- Streaming Responses
- Evaluation Hooks
- Hybrid Search (BM25 + Vector)
- Embedding Caching
- Basic Security / Prompt Injection Protection
"""

# ============================================================
# IMPORTS
# ============================================================

from config.settings import PERSIST_DIRECTORY

from ingestion.loader import load_documents
from ingestion.chunking import chunk_documents, add_metadata
from ingestion.embedding import get_embedding_model

from vectordb.chroma_manager import create_or_load_vector_store, get_vector_retriever

from retrieval.hybrid_retriever import create_bm25_retriever, create_hybrid_retriever
from retrieval.reranker import get_reranker, rerank_documents
from retrieval.query_rewriter import (
    create_query_rewriter,
    get_rewrite_prompt,
    rewrite_query,
)

from llm.model import get_llm_model
from llm.prompts import get_main_rag_prompt
from llm.chains import create_rag_chain, invoke_rag_chain

from memory.chat_memory import create_chat_memory, get_chat_history, save_to_memory

from security.guardrails import is_safe_query, sanitize_query

from evaluation.evaluator import evaluate_response

from utils.helpers import format_context, display_sources, print_header, print_section

# ============================================================
# STEP 1: DOCUMENT INGESTION
# ============================================================


def setup_documents():
    """Load and prepare documents"""
    print_section("STEP 1: DOCUMENT INGESTION")

    # Load documents
    documents = load_documents()
    print(f"✅ Loaded {len(documents)} documents")

    # Chunk documents
    split_docs = chunk_documents(documents)
    print(f"✅ Split into {len(split_docs)} chunks")

    # Add metadata
    split_docs = add_metadata(split_docs)
    print(f"✅ Added metadata to chunks")

    return split_docs


# ============================================================
# STEP 2: VECTOR DATABASE & EMBEDDINGS
# ============================================================


def setup_vector_store(split_docs):
    """Initialize vector store and embeddings"""
    print_section("STEP 2: VECTOR DATABASE & EMBEDDINGS")

    # Get embedding model
    embedding_model = get_embedding_model()
    print(f"✅ Loaded embedding model")

    # Create or load vector store
    vector_store = create_or_load_vector_store(split_docs, embedding_model)
    print(f"✅ Vector store ready (persisted to: {PERSIST_DIRECTORY})")

    # Get vector retriever
    vector_retriever = get_vector_retriever(vector_store)
    print(f"✅ Vector retriever initialized")

    return vector_store, vector_retriever, embedding_model


# ============================================================
# STEP 3: HYBRID RETRIEVAL SETUP
# ============================================================


def setup_hybrid_retrieval(split_docs, vector_retriever):
    """Initialize hybrid retrieval system"""
    print_section("STEP 3: HYBRID RETRIEVAL SETUP")

    # Create BM25 retriever
    bm25_retriever = create_bm25_retriever(split_docs)
    print(f"✅ BM25 retriever initialized")

    # Create hybrid retriever
    hybrid_retriever = create_hybrid_retriever(vector_retriever, bm25_retriever)
    print(f"✅ Hybrid retriever initialized (BM25 + Vector)")

    return hybrid_retriever


# ============================================================
# STEP 4: RE-RANKING SETUP
# ============================================================


def setup_reranker():
    """Initialize re-ranker"""
    print_section("STEP 4: RE-RANKING SETUP")

    reranker = get_reranker()
    print(f"✅ Re-ranker initialized")

    return reranker


# ============================================================
# STEP 5: LLM & CHAIN SETUP
# ============================================================


def setup_llm_and_chains():
    """Initialize LLM and RAG chains"""
    print_section("STEP 5: LLM & CHAIN SETUP")

    # Get LLM model
    llm = get_llm_model()
    print(f"✅ Main LLM initialized")

    # Get query rewriter
    rewriter_llm = create_query_rewriter()
    print(f"✅ Query rewriter LLM initialized")

    # Get prompts
    main_prompt = get_main_rag_prompt()
    rewrite_prompt = get_rewrite_prompt()
    print(f"✅ Prompts loaded")

    # Create RAG chain
    rag_chain = create_rag_chain(main_prompt, llm)
    print(f"✅ RAG chain created")

    return llm, rewriter_llm, main_prompt, rewrite_prompt, rag_chain


# ============================================================
# STEP 6: MEMORY SETUP
# ============================================================


def setup_memory():
    """Initialize conversation memory"""
    print_section("STEP 6: MEMORY SETUP")

    memory = create_chat_memory()
    print(f"✅ Conversation memory initialized")

    return memory


# ============================================================
# STEP 7: CHAT LOOP
# ============================================================


def chat_loop(
    hybrid_retriever, reranker, memory, rewriter_llm, rewrite_prompt, rag_chain
):
    """Main chat loop"""
    print_header("✅ Production Ready RAG System Started")
    print("🔥 Press 0 to Exit\n")

    while True:
        # Get user input
        query = input("You : ")

        if query == "0":
            print("\nExiting RAG system...")
            break

        # Sanitize query
        query = sanitize_query(query)

        # Security check
        if not is_safe_query(query):
            print("\nAI: Unsafe query detected. Please rephrase your question.")
            continue

        # Query rewriting
        print(f"\n🔍 Rewriting query...")
        rewritten_query = rewrite_query(query, rewriter_llm, rewrite_prompt)
        print(f"🔍 Rewritten Query: {rewritten_query}")

        # Hybrid retrieval
        print(f"\n🔎 Retrieving relevant documents...")
        retrieved_docs = hybrid_retriever.invoke(rewritten_query)

        if not retrieved_docs:
            print("\nAI: No relevant documents found.")
            continue

        print(f"📄 Retrieved {len(retrieved_docs)} documents")

        # Re-ranking
        print(f"\n⭐ Re-ranking documents...")
        reranked_docs = rerank_documents(rewritten_query, retrieved_docs, reranker)
        print(f"⭐ Top {len(reranked_docs)} documents selected")

        # Format context
        context = format_context(reranked_docs)

        # Get chat history
        chat_history = get_chat_history(memory)

        # Generate response
        print(f"\n🤖 Generating response...")
        print("\nAI: ", end="")

        response = invoke_rag_chain(rag_chain, chat_history, context, query)
        print(response)

        # Save to memory
        save_to_memory(memory, query, response)

        # Display sources
        display_sources(reranked_docs)

        # Evaluation
        evaluate_response(query, response, reranked_docs)


# ============================================================
# MAIN APPLICATION
# ============================================================


def main():
    """Main application entry point"""
    try:
        # Setup document ingestion
        split_docs = setup_documents()

        # Setup vector store
        vector_store, vector_retriever, embedding_model = setup_vector_store(split_docs)

        # Setup hybrid retrieval
        hybrid_retriever = setup_hybrid_retrieval(split_docs, vector_retriever)

        # Setup re-ranker
        reranker = setup_reranker()

        # Setup LLM and chains
        llm, rewriter_llm, main_prompt, rewrite_prompt, rag_chain = (
            setup_llm_and_chains()
        )

        # Setup memory
        memory = setup_memory()

        # Start chat loop
        chat_loop(
            hybrid_retriever, reranker, memory, rewriter_llm, rewrite_prompt, rag_chain
        )

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        raise


if __name__ == "__main__":
    main()
