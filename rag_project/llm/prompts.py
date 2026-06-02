"""
Prompt templates module for RAG system

WHY?
- Strong prompts reduce hallucination
- Centralized prompt management for easy modification
"""

from langchain_core.prompts import ChatPromptTemplate


def get_main_rag_prompt():
    """
    Get the main RAG system prompt

    WHY?
    - Do not make assumptions
    - Do not hallucinate
    - Provide source references

    Returns:
        ChatPromptTemplate instance
    """
    main_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
You are a helpful AI assistant.

Use ONLY the provided context to answer.

Rules:
- Do not make assumptions
- Do not hallucinate
- If answer is unavailable say:
  "I could not find the answer in the provided documents."

Always provide source references if available.
""",
            ),
            (
                "human",
                """
Conversation History:
{history}

Context:
{context}

Question:
{question}
""",
            ),
        ]
    )
    return main_prompt
