
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import re

def task_func(example_str):
    # Remove text enclosed in square brackets
    cleaned_text = re.sub(r'\[.*?\]', '', example_str)
    
    # Initialize the TfidfVectorizer
    vectorizer = TfidfVectorizer()
    
    # Fit and transform the cleaned text
    tfidf_matrix = vectorizer.fit_transform([cleaned_text])
    
    # Get the feature names (words)
    feature_names = vectorizer.get_feature_names_out()
    
    # Get the TF-IDF scores
    tfidf_scores = tfidf_matrix.toarray()[0]
    
    # Create a dictionary with words as keys and TF-IDF scores as values
    tfidf_dict = dict(zip(feature_names, tfidf_scores))
    
    return tfidf_dict