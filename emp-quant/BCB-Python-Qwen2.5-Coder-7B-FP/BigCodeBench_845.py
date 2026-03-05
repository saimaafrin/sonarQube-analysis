import re
import numpy as np
from collections import Counter
from Levenshtein import ratio
ALPHANUMERIC = re.compile('[\W_]+')
def task_func(text1, text2):
    """
    Calculate the similarity values between two texts based on cosine similarity and Levenshtein ratio.
    
    Args:
    text1 (str): The first text.
    text2 (str): The second text.
    
    Returns:
    tuple: A tuple containing the cosine similarity and Levenshtein ratio as floats.
    """
    # Clean the texts
    text1 = ALPHANUMERIC.sub(' ', text1).lower()
    text2 = ALPHANUMERIC.sub(' ', text2).lower()
    
    # Tokenize the texts
    words1 = text1.split()
    words2 = text2.split()
    
    # Calculate term frequency vectors
    tf1 = np.array(list(Counter(words1).values()))
    tf2 = np.array(list(Counter(words2).values()))
    
    # Normalize the term frequency vectors
    norm1 = np.linalg.norm(tf1)
    norm2 = np.linalg.norm(tf2)
    
    # Calculate cosine similarity
    cosine_similarity = np.dot(tf1, tf2) / (norm1 * norm2) if norm1 != 0 and norm2 != 0 else 0
    
    # Calculate Levenshtein ratio
    levenshtein_ratio = ratio(text1, text2)
    
    return (cosine_similarity, levenshtein_ratio)