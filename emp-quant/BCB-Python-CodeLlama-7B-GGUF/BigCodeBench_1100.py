
import re
from sklearn.feature_extraction.text import TfidfVectorizer

def task_func(texts):
    # Remove URLs from the text documents
    texts = [re.sub(r'https?://\S+', '', text) for text in texts]

    # Create a TfidfVectorizer object
    vectorizer = TfidfVectorizer()

    # Fit and transform the vectorizer to the texts
    X = vectorizer.fit_transform(texts)

    # Get the TF-IDF scores for each word in each document
    scores = X.toarray()

    # Get the unique words (features) across all documents
    features = vectorizer.get_feature_names()

    # Return a tuple of (list of tuples, list of str)
    return (scores, features)