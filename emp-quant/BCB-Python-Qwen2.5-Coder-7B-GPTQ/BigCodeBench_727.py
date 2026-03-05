import re
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
SENTENCES = ['This is a sentence', 'Another sentence here', 'More sentences']
def task_func(s: str) -> np.ndarray:
    # Initialize the CountVectorizer with the predefined sentences
    vectorizer = CountVectorizer(vocabulary={word: i for i, sentence in enumerate(SENTENCES) for word in sentence.split()})
    
    # Transform the input string using the vectorizer
    vectorized = vectorizer.transform([s])
    
    # Convert the transformed result to a numpy array
    result = vectorized.toarray()
    
    return result