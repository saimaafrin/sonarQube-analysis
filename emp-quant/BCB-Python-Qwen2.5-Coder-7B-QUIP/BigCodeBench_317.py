
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import re
def task_func(example_str):
    # Remove text enclosed in square brackets
    example_str = re.sub(r'\[.*?\]', '', example_str)
    
    # Initialize the TfidfVectorizer
    vectorizer = TfidfVectorizer()
    
    # Fit and transform the text
    tfidf = vectorizer.fit_transform([example_str])
    
    # Get the feature names
    feature_names = vectorizer.get_feature_names_out()
    
    # Get the TF-IDF scores
    tfidf_scores = tfidf.toarray()
    
    # Create a dictionary with words as keys and TF-IDF scores as values
    tfidf_dict = dict(zip(feature_names, tfidf_scores[0]))
    
    return tfidf_dict