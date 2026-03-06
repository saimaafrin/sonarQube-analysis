import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import re
def task_func(example_str):
    """
    Extract all texts not enclosed in square brackets into a string and calculate the TF-IDF values
    which are returned as a dictionary.

    Parameters:
    example_str (str): The input string.

    Returns:
    dict: A dictionary with words as keys and TF-IDF scores as values.

    Requirements:
    - sklearn.feature_extraction.text.TfidfVectorizer
    - numpy
    - re

    Example:
    >>> tfidf_scores = task_func("Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003] Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]")
    >>> print(tfidf_scores)
    {'dog': 0.3779644730092272, 'josie': 0.3779644730092272, 'mugsy': 0.3779644730092272, 'smith': 0.7559289460184544}
    """
    # Extract all texts not enclosed in square brackets into a string
    example_str = re.sub(r'\[[^\]]*\]', '', example_str)

    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer(min_df=1, max_df=1.0, stop_words='english')

    # Create a TF-IDF matrix
    tfidf_matrix = vectorizer.fit_transform([example_str])

    # Create a dictionary with words as keys and TF-IDF scores as values
    tfidf_scores = dict(zip(vectorizer.get_feature_names(), tfidf_matrix[0]))

    return tfidf_scores