
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import re

def task_func(example_str):
    # Create a TfidfVectorizer object
    vectorizer = TfidfVectorizer(stop_words=['[', ']'])

    # Tokenize the text
    tokens = vectorizer.fit_transform(example_str)

    # Calculate the TF-IDF scores
    scores = vectorizer.fit_transform(tokens)

    # Create a dictionary with words as keys and TF-IDF scores as values
    dict = {word: score for word, score in zip(vectorizer.get_feature_names(), scores)}

    return dict