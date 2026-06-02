"""
LLM model initialization module for RAG system
"""

from langchain_mistralai import ChatMistralAI
from config.settings import LLM_MODEL, LLM_TEMPERATURE, LLM_STREAMING


def get_llm_model(
    model: str = LLM_MODEL,
    temperature: float = LLM_TEMPERATURE,
    streaming: bool = LLM_STREAMING,
):
    """
    Initialize and return main LLM instance

    Args:
        model: LLM model name
        temperature: Temperature for generation (0-1)
        streaming: Whether to enable streaming responses

    Returns:
        ChatMistralAI instance
    """
    llm = ChatMistralAI(model=model, temperature=temperature, streaming=streaming)
    return llm
