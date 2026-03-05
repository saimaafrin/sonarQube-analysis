
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
    
    # Count the term frequencies
    counter1 = Counter(words1)
    counter2 = Counter(words2)
    
    # Get the unique words from both texts
    unique_words = set(counter1.keys()).union(set(counter2.keys()))
    
    # Create vectors for each text based on term frequency
    vector1 = np.array([counter1[word] for word in unique_words])
    vector2 = np.array([counter2[word] for word in unique_words])
    
    # Calculate the cosine similarity
    dot_product = np.dot(vector1, vector2)
    norm1 = np.linalg.norm(vector1)
    norm2 = np.linalg.norm(vector2)
    cosine_similarity = dot_product / (norm1 * norm2)
    
    # Calculate the Levenshtein ratio
    levenshtein_ratio = ratio(text1, text2)
    
    return (cosine_similarity, levenshtein_ratio)