
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import re

def task_func(example_str):
    # Extract all texts not enclosed in square brackets
    texts = re.findall(r'\[.*?\]', example_str)
    # Calculate TF-IDF values
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(texts)
    # Return TF-IDF values as a dictionary
    return {word: tfidf[i] for i, word in enumerate(vectorizer.get_feature_names())}