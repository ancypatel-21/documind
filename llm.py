def generate_answer(query, retrieved_docs):
    if not retrieved_docs:
        return "I could not find relevant information in the documents."

    context = " ".join(retrieved_docs)

    # simple, polished offline answer generator
    return (
        f"Question: {query}\n\n"
        f"Based on the retrieved context, the most relevant information is:\n"
        f"{context}\n\n"
        f"In short, the documents suggest that this topic is related to the query above."
    )