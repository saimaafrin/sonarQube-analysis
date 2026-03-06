
import re
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

# Constants
SENTENCES = ['This is a sentence', 'Another sentence here', 'More sentences']

def task_func(s: str) -> np.ndarray:
    # Combine all sentences including the input string
    combined_sentences = SENTENCES + [s]
    
    # Initialize the CountVectorizer
    vectorizer = CountVectorizer()
    
    # Fit and transform the combined sentences
    X = vectorizer.fit_transform(combined_sentences)
    
    # Get the last row which corresponds to the input string
    result_vector = X[-1].toarray()
    
    return result_vector