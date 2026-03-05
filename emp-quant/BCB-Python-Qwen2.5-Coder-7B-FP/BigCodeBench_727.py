import re
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
SENTENCES = ['This is a sentence', 'Another sentence here', 'More sentences']
def task_func(s: str) -> np.ndarray:
    # Initialize the CountVectorizer
    vectorizer = CountVectorizer()
    
    # Fit and transform the predefined sentences
    X = vectorizer.fit_transform(SENTENCES)
    
    # Transform the input string
    s_transformed = vectorizer.transform([s])
    
    # Convert the transformed input to a numpy array
    result = s_transformed.toarray()
    
    return result