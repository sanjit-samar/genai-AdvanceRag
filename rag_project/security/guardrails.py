"""
Security and guardrails module for RAG system

WHY?
- Prevent malicious prompts like "Ignore previous instructions"
- Basic protection layer against prompt injection attacks
- Sanitize user inputs
"""

from config.settings import BLOCKED_PATTERNS


def is_safe_query(query: str, blocked_patterns: list = BLOCKED_PATTERNS):
    """
    Check if query is safe and doesn't contain blocked patterns

    WHY?
    - Prevent prompt injection attacks
    - Block attempts to bypass system instructions

    Args:
        query: User query to validate
        blocked_patterns: List of patterns to block

    Returns:
        Boolean indicating if query is safe
    """
    query_lower = query.lower()

    for pattern in blocked_patterns:
        if pattern in query_lower:
            return False

    return True


def sanitize_query(query: str) -> str:
    """
    Sanitize user query

    Args:
        query: User query

    Returns:
        Sanitized query string
    """
    # Remove leading/trailing whitespace
    query = query.strip()

    # Remove excessive whitespace
    query = " ".join(query.split())

    return query
