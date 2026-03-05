
import re
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

# Constants
SENTENCES = ['This is a sentence', 'Another sentence here', 'More sentences']

def task_func(s: str) -> np.ndarray:
    # Create a CountVectorizer object
    vectorizer = CountVectorizer()
    
    # Fit the vectorizer on the predefined sentences
    vectorizer.fit(SENTENCES)
    
    # Transform the input string using the fitted vectorizer
    vectorized_string = vectorizer.transform([s])
    
    # Convert the transformed string to a numpy array
    result = vectorized_string.toarray()
    
    return result