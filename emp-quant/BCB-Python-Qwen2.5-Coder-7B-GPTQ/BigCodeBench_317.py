import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import re
def task_func(example_str):
    # Remove text enclosed in square brackets
    cleaned_str = re.sub(r'\[.*?\]', '', example_str)
    
    # Tokenize the cleaned string
    tokens = cleaned_str.split()
    
    # Initialize TfidfVectorizer
    vectorizer = TfidfVectorizer()
    
    # Fit and transform the tokens
    tfidf_matrix = vectorizer.fit_transform(tokens)
    
    # Get feature names
    feature_names = vectorizer.get_feature_names_out()
    
    # Get the TF-IDF scores
    tfidf_scores = tfidf_matrix.toarray()
    
    # Create a dictionary with words as keys and TF-IDF scores as values
    tfidf_dict = dict(zip(feature_names, tfidf_scores.flatten()))
    
    return tfidf_dict