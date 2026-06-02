"""
Chat memory module for RAG system

WHY?
- Makes chatbot stateful
- Remembers previous questions
- Supports follow-up conversations
"""

from langchain.memory import ConversationBufferMemory


def create_chat_memory(return_messages: bool = True):
    """
    Create conversation memory for chat history

    Args:
        return_messages: Whether to return messages or strings

    Returns:
        ConversationBufferMemory instance
    """
    memory = ConversationBufferMemory(return_messages=return_messages)
    return memory


def get_chat_history(memory):
    """
    Get chat history from memory

    Args:
        memory: ConversationBufferMemory instance

    Returns:
        Dict with chat history
    """
    chat_history = memory.load_memory_variables({})
    return chat_history


def save_to_memory(memory, user_input: str, ai_output: str):
    """
    Save user input and AI output to memory

    Args:
        memory: ConversationBufferMemory instance
        user_input: User's message
        ai_output: AI's response
    """
    memory.save_context({"input": user_input}, {"output": ai_output})
