"""
Helper utilities for RAG system
"""


def format_context(documents):
    """
    Format retrieved documents as context for LLM

    WHY?
    - Users should know source and chunk information
    - Enables source tracking and traceability

    Args:
        documents: List of Document objects

    Returns:
        Formatted context string
    """
    formatted = []

    for doc in documents:
        source = doc.metadata.get("source", "Unknown")
        chunk_id = doc.metadata.get("chunk_id", "NA")

        formatted.append(f"""
SOURCE: {source}
CHUNK_ID: {chunk_id}

CONTENT:
{doc.page_content}
""")

    return "\n\n".join(formatted)


def display_sources(documents):
    """
    Display source information for retrieved documents

    Args:
        documents: List of Document objects
    """
    print("\n📚 SOURCES USED:")

    for doc in documents:
        source = doc.metadata.get("source", "Unknown")
        chunk_id = doc.metadata.get("chunk_id", "NA")

        print(f"""
Source File : {source}
Chunk ID    : {chunk_id}
""")


def print_header(text: str, char: str = "=", width: int = 60):
    """
    Print formatted header

    Args:
        text: Header text
        char: Character for header border
        width: Total width of header
    """
    print(f"\n{char * width}")
    print(f"{text.center(width)}")
    print(f"{char * width}\n")


def print_section(title: str):
    """
    Print section separator

    Args:
        title: Section title
    """
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print(f"{'=' * 60}\n")
