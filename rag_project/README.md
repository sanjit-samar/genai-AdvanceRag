# Production-Ready RAG (Retrieval Augmented Generation) System

A modular, scalable implementation of a production-ready RAG pipeline with advanced features including hybrid search, query rewriting, re-ranking, and conversation memory.

## 📁 Project Structure

```
rag_project/
│
├── app.py                          # Main application & chat loop
│
├── config/
│   └── settings.py                 # Configuration & environment variables
│
├── ingestion/                      # Document loading and processing
│   ├── loader.py                   # PDF document loading
│   ├── chunking.py                 # Text splitting & metadata
│   └── embedding.py                # Embedding model initialization
│
├── vectordb/                       # Vector database management
│   └── chroma_manager.py           # Chroma vector store operations
│
├── retrieval/                      # Document retrieval system
│   ├── hybrid_retriever.py         # BM25 + Vector hybrid search
│   ├── reranker.py                 # Document re-ranking with CrossEncoder
│   └── query_rewriter.py           # Query improvement & rewriting
│
├── llm/                            # Language model components
│   ├── model.py                    # LLM initialization (Mistral)
│   ├── prompts.py                  # Prompt templates
│   └── chains.py                   # LLM chains composition
│
├── memory/                         # Conversation state
│   └── chat_memory.py              # Conversation buffer memory
│
├── security/                       # Safety & protection
│   └── guardrails.py               # Prompt injection protection
│
├── evaluation/                     # System evaluation
│   └── evaluator.py                # Evaluation hooks & metrics
│
├── utils/                          # Helper utilities
│   └── helpers.py                  # Formatting & display utilities
│
├── data/                           # Data storage
│   └── sample.pdf                  # Sample document for RAG
│
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## 🚀 Quick Start

### 1. Setup Environment

```bash
# Navigate to project directory
cd rag_project

# Create virtual environment (if not already done)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configuration

Create a `.env` file in the root directory with your API keys:

```env
MISTRAL_API_KEY=your_api_key_here
```

### 4. Add Your Document

Place your PDF file in the `data/` folder or update the `PDF_PATH` in `config/settings.py`:

```python
PDF_PATH = "data/your_document.pdf"
```

### 5. Run the Application

```bash
python app.py
```

## 🎯 Key Features

### 1. **Hybrid Search (BM25 + Vector)**
- Combines exact keyword matching (BM25) with semantic search (Vector embeddings)
- Ensemble retriever with configurable weights
- Better coverage of both keyword and semantic queries

### 2. **Document Re-ranking**
- Uses CrossEncoder for better relevance scoring
- Improves ranking quality of retrieved documents
- Reduces hallucination by using highly relevant context

### 3. **Query Rewriting**
- Converts vague user questions into clear search queries
- Improves retrieval quality
- Handles follow-up questions and context

### 4. **Conversation Memory**
- Maintains chat history for context-aware responses
- Supports follow-up conversations
- Buffer memory for state management

### 5. **Security & Guardrails**
- Prompt injection protection
- Query safety validation
- Input sanitization
- Blocked pattern detection

### 6. **Evaluation Hooks**
- Response quality evaluation
- Retrieval quality metrics
- Extensible evaluation framework

### 7. **Production-Ready Features**
- Persistent vector store caching
- Streaming responses
- Source citations and traceability
- Comprehensive logging and debugging

## 📚 Module Documentation

### config/settings.py
Centralized configuration management for:
- API keys and environment variables
- Model parameters (temperature, chunk size, etc.)
- Retrieval configuration (weights, top-k values)
- Security settings

### ingestion/
- **loader.py**: Loads PDF documents using LangChain's PyPDFLoader
- **chunking.py**: Splits documents into overlapping chunks to preserve context
- **embedding.py**: Initializes HuggingFace embeddings for semantic search

### vectordb/chroma_manager.py
- Creates or loads persistent Chroma vector store
- Manages vector retrieval with MMR (Maximal Marginal Relevance)
- Handles embedding caching to avoid recomputation

### retrieval/
- **hybrid_retriever.py**: Combines BM25 and vector search using EnsembleRetriever
- **reranker.py**: Re-ranks retrieved documents using CrossEncoder
- **query_rewriter.py**: Rewrites queries using LLM for better retrieval

### llm/
- **model.py**: Initializes ChatMistralAI with streaming support
- **prompts.py**: System and user prompts for RAG pipeline
- **chains.py**: Composes LangChain LCEL chains for retrieval and generation

### memory/chat_memory.py
- Manages conversation buffer memory
- Saves and loads chat history
- Maintains context for multi-turn conversations

### security/guardrails.py
- Validates user queries for safety
- Detects common prompt injection patterns
- Sanitizes user input

### evaluation/evaluator.py
- Evaluates response quality
- Calculates retrieval metrics
- Provides evaluation hooks for monitoring

### utils/helpers.py
- Formats retrieved documents for LLM context
- Displays source citations
- Pretty-prints sections and headers

## 🔄 Workflow

```
User Input
    ↓
Query Safety Check (Security)
    ↓
Query Rewriting (Query Rewriter)
    ↓
Hybrid Retrieval (BM25 + Vector)
    ↓
Document Re-ranking (CrossEncoder)
    ↓
Context Formatting (Helpers)
    ↓
Memory Fetch (Chat Memory)
    ↓
RAG Chain Invocation (LLM)
    ↓
Response Generation
    ↓
Memory Save (Chat Memory)
    ↓
Source Display & Evaluation
```

## ⚙️ Configuration Guide

### Adjust Chunk Size
In `config/settings.py`:
```python
CHUNK_SIZE = 500      # Increase for larger chunks
CHUNK_OVERLAP = 50    # Increase for more context overlap
```

### Adjust Retrieval Parameters
```python
# Vector retrieval
VECTOR_K = 4          # Number of vectors to retrieve
VECTOR_LAMBDA_MULT = 0.7  # Diversity parameter (0-1)

# Hybrid search weights
ENSEMBLE_WEIGHTS = [0.4, 0.6]  # [BM25, Vector]
```

### Change LLM Model
```python
LLM_MODEL = "mistral-small-2603"  # Change to different Mistral model
LLM_TEMPERATURE = 0               # 0 for deterministic, 1 for creative
```

## 🔐 Security Considerations

- **Prompt Injection Protection**: Basic pattern matching for common attacks
- **Input Validation**: Query sanitization and safety checks
- **Source Tracking**: All responses include source citations
- **Context Limitation**: Only uses provided documents to avoid hallucination

For production, consider:
- Rate limiting
- User authentication
- Output filtering
- Advanced prompt injection detection

## 📊 Evaluation

The system includes evaluation hooks for:
- Answer quality assessment
- Retrieval quality metrics
- Response length and token counting
- Integration with frameworks like Ragas, DeepEval, or TruLens

Extend `evaluation/evaluator.py` for custom metrics.

## 🚨 Troubleshooting

### Import Errors
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

### API Key Issues
- Ensure `.env` file is in the project root
- Verify `MISTRAL_API_KEY` is set correctly
- Check API key permissions and quota

### Vector Store Issues
- Delete `production_rag_db` folder to reset the vector store
- Ensure `sample.pdf` or specified PDF exists

### Memory Issues
- Reduce `CHUNK_SIZE` or `VECTOR_FETCH_K` for lower memory usage
- Consider using summary memory instead of buffer memory

## 🤝 Extending the System

### Add Custom Retriever
Create new file in `retrieval/`:
```python
def create_custom_retriever(...):
    # Your implementation
    pass
```

### Add Custom Evaluation
Extend `evaluation/evaluator.py`:
```python
def custom_evaluation(...):
    # Your evaluation logic
    pass
```

### Add New LLM Model
Update `llm/model.py`:
```python
def get_alternative_llm(...):
    # Initialize your model
    pass
```

## 📝 License

[Add your license here]

## 💬 Support

For issues or questions, please create an issue or contact the development team.

---

**Last Updated**: June 2024
**Python Version**: 3.8+
**Status**: Production-Ready
