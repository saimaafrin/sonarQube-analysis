
import re
import numpy as np
from collections import Counter
from Levenshtein import ratio

# Constants
ALPHANUMERIC = re.compile('[\W_]+')

def task_func(text1, text2):
    # Clean the texts
    text1 = ALPHANUMERIC.sub(' ', text1).lower()
    text2 = ALPHANUMERIC.sub(' ', text2).lower()
    
    # Tokenize the texts
    words1 = text1.split()
    words2 = text2.split()
    
    # Create term frequency vectors
    tf1 = np.array([words1.count(word) for word in set(words1)])
    tf2 = np.array([words2.count(word) for word in set(words2)])
    
    # Calculate cosine similarity
    cosine_similarity = np.dot(tf1, tf2) / (np.linalg.norm(tf1) * np.linalg.norm(tf2))
    
    # Calculate Levenshtein ratio
    levenshtein_ratio = ratio(text1, text2)
    
    return (cosine_similarity, levenshtein_ratio)