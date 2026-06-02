"""
Evaluation module for RAG system

WHY?
- Production systems need evaluation
- Track system performance
- Identify issues with retrieval and generation

Evaluation Frameworks:
- Ragas
- DeepEval
- TruLens

Here we add simple logging hooks for basic evaluation.
"""


def evaluate_response(question: str, answer: str, documents, verbose: bool = True):
    """
    Evaluate RAG response quality

    Args:
        question: User question
        answer: Generated answer
        documents: Retrieved documents
        verbose: Whether to print evaluation results

    Returns:
        Dict with evaluation metrics
    """
    evaluation_metrics = {
        "question": question,
        "answer_length": len(answer),
        "retrieved_chunks": len(documents),
        "answer_tokens": len(answer.split()),
    }

    if verbose:
        print("\n========== EVALUATION ==========")
        print(f"Question: {question}")
        print(f"Retrieved Chunks: {len(documents)}")
        print(f"Answer Length: {len(answer)}")
        print("================================")

    return evaluation_metrics


def evaluate_retrieval(question: str, retrieved_docs, relevant_docs=None):
    """
    Evaluate retrieval quality

    Args:
        question: User question
        retrieved_docs: Documents retrieved by the system
        relevant_docs: Ground truth relevant documents (optional)

    Returns:
        Dict with retrieval metrics
    """
    retrieval_metrics = {
        "question": question,
        "num_retrieved": len(retrieved_docs),
    }

    # If relevant docs provided, calculate recall
    if relevant_docs:
        relevant_ids = {doc.metadata.get("chunk_id") for doc in relevant_docs}
        retrieved_ids = {doc.metadata.get("chunk_id") for doc in retrieved_docs}

        if relevant_ids:
            recall = len(retrieved_ids & relevant_ids) / len(relevant_ids)
            retrieval_metrics["recall"] = recall

    return retrieval_metrics
