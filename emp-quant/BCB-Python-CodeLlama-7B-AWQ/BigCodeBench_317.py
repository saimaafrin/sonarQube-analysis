import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import re
def task_func(example_str):
    """
    Extract all texts not enclosed in square brackets into a string and calculate the TF-IDF values which are returned as a dictionary.
    :param example_str: A string containing texts enclosed in square brackets.
    :return: A dictionary with words as keys and TF-IDF scores as values.
    """
    # Extract all texts not enclosed in square brackets into a string
    texts = re.findall(r'\[.*?\]', example_str)
    text = ' '.join(texts)

    # Create a TfidfVectorizer object
    vectorizer = TfidfVectorizer()

    # Fit and transform the text data
    X = vectorizer.fit_transform(text)

    # Get the TF-IDF scores as a dictionary
    tfidf_scores = dict(zip(vectorizer.get_feature_names(), X.toarray().ravel()))

    return tfidf_scores
example_str = 'This is a [text] enclosed in square brackets.'