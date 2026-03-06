
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import re

def task_func(example_str):
    # Extract all texts not enclosed in square brackets
    texts = re.findall(r'(?<!\[).*?(?!\])', example_str)

    # Create a TfidfVectorizer object
    vectorizer = TfidfVectorizer()

    # Fit and transform the texts
    X = vectorizer.fit_transform(texts)

    # Get the TF-IDF scores as a dictionary
    tfidf_scores = dict(zip(vectorizer.get_feature_names(), X.toarray().ravel()))

    return tfidf_scores