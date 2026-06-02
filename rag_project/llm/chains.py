"""
LLM chains module for RAG system

WHY?
- Cleaner architecture
- Easier to compose and test chains
- Structured RAG chain for better scaling
"""

from langchain_core.output_parsers import StrOutputParser


def create_rag_chain(prompt, llm):
    """
    Create the main RAG chain

    Args:
        prompt: ChatPromptTemplate instance
        llm: LLM instance

    Returns:
        Runnable chain (prompt | llm | parser)
    """
    output_parser = StrOutputParser()
    rag_chain = prompt | llm | output_parser
    return rag_chain


def invoke_rag_chain(rag_chain, history: str, context: str, question: str):
    """
    Invoke RAG chain with inputs

    Args:
        rag_chain: RAG chain instance
        history: Conversation history
        context: Retrieved context
        question: User question

    Returns:
        Generated response string
    """
    response = rag_chain.invoke(
        {"history": history, "context": context, "question": question}
    )
    return response
