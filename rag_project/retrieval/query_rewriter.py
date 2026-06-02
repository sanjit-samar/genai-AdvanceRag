"""
Query rewriting module for RAG system

WHY?
- Users ask vague questions
- Query rewriting improves retrieval quality
- Converts user questions into clear standalone search queries
"""

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config.settings import LLM_MODEL, LLM_TEMPERATURE


def create_query_rewriter(model: str = LLM_MODEL, temperature: float = LLM_TEMPERATURE):
    """
    Create query rewriter LLM instance

    Args:
        model: LLM model name
        temperature: Temperature for generation

    Returns:
        ChatMistralAI instance
    """
    rewriter_llm = ChatMistralAI(model=model, temperature=temperature)
    return rewriter_llm


def get_rewrite_prompt():
    """
    Get the prompt template for query rewriting

    Returns:
        ChatPromptTemplate instance
    """
    rewrite_prompt = ChatPromptTemplate.from_template("""
Rewrite the user question into a clear standalone search query.

Question:
{question}
""")
    return rewrite_prompt


def rewrite_query(query: str, rewriter_llm, rewrite_prompt):
    """
    Rewrite user query to improve retrieval

    Args:
        query: Original user query
        rewriter_llm: Query rewriter LLM instance
        rewrite_prompt: Prompt template for rewriting

    Returns:
        Rewritten query string
    """
    output_parser = StrOutputParser()
    rewrite_chain = rewrite_prompt | rewriter_llm | output_parser
    rewritten_query = rewrite_chain.invoke({"question": query})
    return rewritten_query
