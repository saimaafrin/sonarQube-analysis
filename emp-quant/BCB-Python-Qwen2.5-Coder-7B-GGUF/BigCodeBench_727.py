
import re
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

# Constants
SENTENCES = ['This is a sentence', 'Another sentence here', 'More sentences']

def task_func(s: str) -> np.ndarray:
    # Create a CountVectorizer object
    vectorizer = CountVectorizer()
    
    # Fit and transform the predefined sentences
    X = vectorizer.fit_transform(SENTENCES)
    
    # Transform the input string
    s_transformed = vectorizer.transform([s])
    
    # Return the transformed string as a numpy array
    return s_transformed.toarray()