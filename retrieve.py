from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def retrieve_top_k(query, documents, k=3):
    corpus = documents + [query]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)

    doc_vectors = tfidf_matrix[:-1]
    query_vector = tfidf_matrix[-1]

    scores = cosine_similarity(query_vector, doc_vectors).flatten()
    ranked_indices = scores.argsort()[::-1]

    results = []
    for idx in ranked_indices[:k]:
        if scores[idx] > 0:
            results.append((documents[idx], scores[idx]))

    return results