# DocuMind

LLM-powered document Q&A system using retrieval-augmented generation (RAG).

---

## Overview

DocuMind is a simplified Retrieval-Augmented Generation (RAG) system that enables users to query a collection of documents and receive context-aware answers. The system retrieves the most relevant document chunks using similarity-based ranking and generates responses based on the retrieved context.

This project demonstrates the core pipeline used in modern AI-powered search and document understanding systems.

---

## Key Features

* Document ingestion and preprocessing
* Query-based document retrieval
* TF-IDF–based similarity ranking
* Top-K relevant chunk selection
* Answer generation using retrieved context
* Modular and extensible pipeline design

---

## System Architecture

```id="9h6y7c"
User Query → Vectorization → Similarity Search → Top-K Retrieval → Answer Generation
```

---

## How It Works

### 1. Document Ingestion

`ingest.py` loads and prepares a set of documents for querying.

---

### 2. Query Processing

User input is taken as a query and processed for retrieval.

---

### 3. Retrieval (TF-IDF + Cosine Similarity)

`retrieve.py` converts documents and the query into vector representations and computes similarity scores to identify the most relevant content.

---

### 4. Answer Generation

`llm.py` generates a response using the retrieved documents as context.

---

## Project Structure

```id="p4hxg7"
documind/
├── main.py
├── ingest.py
├── retrieve.py
├── llm.py
└── README.md
```

---

## Run the Project

```bash id="7p0u3c"
python3 main.py
```

---

## Sample Output

```id="d7rfp3"
Enter your question: What is RAG?

Retrieved Documents:
- Retrieval-Augmented Generation improves LLM responses. (score: 0.72)

Final Answer:
Question: What is RAG?

Based on the retrieved context, the most relevant information is:
Retrieval-Augmented Generation improves LLM responses.

In short, the documents suggest that this topic is related to the query above.
```

---

## Tech Stack

* Python
* scikit-learn (TF-IDF, cosine similarity)
* Basic NLP techniques

---

## Key Learnings

* Building a Retrieval-Augmented Generation pipeline
* Implementing document similarity using TF-IDF
* Ranking and selecting relevant content
* Designing modular AI pipelines
* Understanding how LLM-based Q&A systems work

---

## Future Improvements

* Replace TF-IDF with embedding models
* Integrate a real LLM API (OpenAI / Claude)
* Add PDF ingestion and chunking
* Store embeddings in a vector database
* Improve answer generation with prompt engineering

---

## Author

Ancy Patel
