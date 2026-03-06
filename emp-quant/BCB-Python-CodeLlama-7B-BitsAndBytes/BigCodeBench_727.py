
import re
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

# Constants
SENTENCES = ['This is a sentence', 'Another sentence here', 'More sentences']

def task_func(s: str) -> np.ndarray:
    # Split the string into words
    words = re.split(r'\W+', s)

    # Create a CountVectorizer object
    vectorizer = CountVectorizer()

    # Fit the vectorizer to the sentences
    vectorizer.fit(SENTENCES)

    # Transform the words into a vector
    vector = vectorizer.transform(words)

    # Return the vectorized string as a numpy array
    return vector.toarray()