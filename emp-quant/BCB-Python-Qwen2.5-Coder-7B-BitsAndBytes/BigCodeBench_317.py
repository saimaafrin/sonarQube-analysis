
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import re

def task_func(example_str):
    # Extract text not enclosed in square brackets
    pattern = r'\[(.*?)\]'
    cleaned_text = re.sub(pattern, '', example_str)
    
    # Initialize TfidfVectorizer
    vectorizer = TfidfVectorizer()
    
    # Fit and transform the cleaned text
    tfidf_matrix = vectorizer.fit_transform([cleaned_text])
    
    # Get feature names
    feature_names = vectorizer.get_feature_names_out()
    
    # Convert to dense array for easier manipulation
    tfidf_array = tfidf_matrix.toarray()[0]
    
    # Create a dictionary of word-TF-IDF pairs
    tfidf_dict = {feature_names[i]: tfidf_array[i] for i in range(len(feature_names))}
    
    return tfidf_dict