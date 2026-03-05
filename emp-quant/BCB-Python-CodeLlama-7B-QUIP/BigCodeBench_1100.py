
import re
from sklearn.feature_extraction.text import TfidfVectorizer

def task_func(texts):
    # Remove URLs from the text documents
    texts = [re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[0-9][0-9][0-9])+[.]+[.]+[.]', '', text) for text in texts]

    # Create a TfidfVectorizer object
    vectorizer = TfidfVectorizer(stop_words=[], max_df=0.9, max_ngram_range=2)

    # Fit the vectorizer to the texts
    vectorizer.fit(texts)

    # Get the TF-IDF scores for each word in each document
    scores = vectorizer.transform(texts).todense()

    # Get the unique words (features) across all documents
    features = vectorizer.get_feature_names()

    # Return a tuple of (list of tuples, list of str)
    return (scores, features)