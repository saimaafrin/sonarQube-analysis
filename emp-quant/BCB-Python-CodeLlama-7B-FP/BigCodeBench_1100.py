import re
from sklearn.feature_extraction.text import TfidfVectorizer
def task_func(texts):
    # Remove URLs from the text documents
    texts = [re.sub(r'https?://\S+|www\.\S+', '', text) for text in texts]

    # Create a TfidfVectorizer object
    vectorizer = TfidfVectorizer()

    # Fit and transform the TfidfVectorizer object to the texts
    tfidf_matrix = vectorizer.fit_transform(texts)

    # Extract the TF-IDF scores for each word in each document
    tfidf_scores = tfidf_matrix.toarray()

    # Extract the unique words (features) across all documents
    unique_words = vectorizer.get_feature_names()

    # Round the TF-IDF scores to 8 decimal places for precision
    tfidf_scores = np.round(tfidf_scores, 8)

    # Return a tuple of (list of tuples, list of str)
    return (tfidf_scores, unique_words)
texts = [
    'This is a sample text document.',
    'This is another sample text document.',
    'This is a third sample text document.',
]