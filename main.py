from ingest import load_documents
from retrieve import retrieve_top_k
from llm import generate_answer

documents = load_documents()

query = input("Enter your question: ")

results = retrieve_top_k(query, documents, k=3)

print("\nRetrieved Documents:\n")
retrieved_texts = []
for doc, score in results:
    print(f"- {doc} (score: {score:.4f})")
    retrieved_texts.append(doc)

answer = generate_answer(query, retrieved_texts)

print("\nFinal Answer:\n")
print(answer)