# Quick Start Guide

Get your RAG system running in 5 minutes!

## Step 1: Navigate to Project
```bash
cd d:\Ai\genai-AdvanceRag\rag_project
```

## Step 2: Activate Virtual Environment
```bash
# You already have one at ../../my_env/
# Or create new one:
python -m venv venv
venv\Scripts\activate
```

## Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

**Expected packages:**
- langchain==0.3.0
- langchain-mistralai==0.1.0
- sentence-transformers==3.0.0
- chromadb==0.4.0
- pypdf==4.0.0
- python-dotenv==1.0.0

## Step 4: Setup Environment Variables
```bash
# Copy the example file
copy .env.example .env

# Edit .env and add your Mistral API key:
MISTRAL_API_KEY=your_api_key_here
```

Get your API key from: https://console.mistral.ai/

## Step 5: Add Your Document
```bash
# Option 1: Place PDF in data/ folder
copy your_document.pdf data/sample.pdf

# Option 2: Update config/settings.py
# Change: PDF_PATH = "data/your_path.pdf"
```

## Step 6: Run the Application
```bash
python app.py
```

You should see:
```
==================================================
           STEP 1: DOCUMENT INGESTION
==================================================

✅ Loaded X documents
✅ Split into Y chunks
✅ Added metadata to chunks

[More setup steps...]

✅ Production Ready RAG System Started
🔥 Press 0 to Exit

You : 
```

## Step 7: Ask Questions!

```
You : What is the main topic of the document?
🔍 Rewritten Query: What are the primary subjects discussed?
📄 Retrieved 4 documents
⭐ Top 4 documents selected
🤖 Generating response...

AI: Based on the provided context, the main topics are...

📚 SOURCES USED:
Source File : sample.pdf
Chunk ID    : 5

========== EVALUATION ==========
Question: What is the main topic of the document?
Retrieved Chunks: 4
Answer Length: 245
================================
```

## Troubleshooting

### Issue: "ModuleNotFoundError"
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: "MISTRAL_API_KEY not found"
```bash
# Check .env file exists and has your key:
cat .env
```

### Issue: "sample.pdf not found"
```bash
# Add your PDF to data/ folder:
mkdir data
copy your_file.pdf data/sample.pdf
```

### Issue: "No module named 'config'"
```bash
# Make sure you're in rag_project folder:
cd rag_project
python app.py
```

## File Structure Reminder

```
rag_project/
├── app.py              ← Run this: python app.py
├── config/
│   └── settings.py     ← Change configuration here
├── data/
│   └── sample.pdf      ← Add your document here
├── ingestion/
├── retrieval/
├── llm/
├── memory/
├── security/
├── evaluation/
├── utils/
├── vectordb/
├── requirements.txt    ← pip install -r requirements.txt
├── .env.example        ← Copy to .env
└── README.md           ← Full documentation
```

## Useful Configuration Changes

### Use a Different PDF
```python
# In config/settings.py, line 1
PDF_PATH = "data/my_document.pdf"
```

### Adjust Chunk Size
```python
# In config/settings.py
CHUNK_SIZE = 1000      # Larger chunks
CHUNK_OVERLAP = 100    # More overlap
```

### Change LLM Temperature
```python
# In config/settings.py
LLM_TEMPERATURE = 0.5  # 0=deterministic, 1=creative
```

## Environment Variables

Required:
- `MISTRAL_API_KEY` - Your Mistral API key

Optional:
- `OPENAI_API_KEY` - For future use
- `HUGGINGFACE_API_KEY` - For private models

## What Each Folder Does

| Folder | Purpose |
|--------|---------|
| config | Settings and environment |
| ingestion | Load and chunk documents |
| vectordb | Store embeddings |
| retrieval | Find relevant documents |
| llm | Run language models |
| memory | Remember conversations |
| security | Prevent attacks |
| evaluation | Track performance |
| utils | Helper functions |
| data | Input documents |

## Commands Cheat Sheet

```bash
# Setup
cd rag_project
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Configuration
copy .env.example .env
# Edit .env with your API key

# Run
python app.py

# Exit (in app)
You : 0

# Exit terminal
ctrl + c
```

## What Happens When You Run the App

1. **Loads Document** - Reads sample.pdf
2. **Chunks Text** - Splits into 500-char chunks
3. **Creates Embeddings** - Converts to vectors
4. **Sets Up Database** - Stores in Chroma
5. **Initializes Retrievers** - BM25 and Vector search
6. **Loads LLM** - Prepares Mistral model
7. **Ready for Chat** - Waits for your questions

## Next Steps

- Read [README.md](README.md) for full documentation
- Check [REFACTORING_SUMMARY.md](REFACTORING_SUMMARY.md) for architecture details
- Explore individual modules to understand the code
- Customize configuration in [config/settings.py](config/settings.py)

## Need Help?

1. Check the error message carefully
2. Verify MISTRAL_API_KEY is set
3. Ensure dependencies are installed
4. Check PDF file exists
5. Read README.md for detailed docs

---

**You're all set! 🚀 Start with: `python app.py`**
