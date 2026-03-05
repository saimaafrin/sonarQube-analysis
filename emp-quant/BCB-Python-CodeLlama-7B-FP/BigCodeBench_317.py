import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import re
def task_func(example_str):
    """
    Extract all texts not enclosed in square brackets into a string and calculate the TF-IDF values which are returned as a dictionary.
    """
    # Extract all texts not enclosed in square brackets into a string
    text = re.sub(r'\[[^]]*\]', '', example_str)

    # Create a TfidfVectorizer object
    vectorizer = TfidfVectorizer()

    # Fit and transform the text data
    X = vectorizer.fit_transform(text)

    # Get the TF-IDF scores
    scores = vectorizer.idf_

    # Create a dictionary with words as keys and TF-IDF scores as values
    dict = {word: score for word, score in zip(vectorizer.get_feature_names(), scores)}

    return dict
example_str = "This is an example string [with enclosed text]."