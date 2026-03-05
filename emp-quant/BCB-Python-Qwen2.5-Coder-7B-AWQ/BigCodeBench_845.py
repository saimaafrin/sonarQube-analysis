import re
import numpy as np
from collections import Counter
from Levenshtein import ratio
ALPHANUMERIC = re.compile('[\W_]+')
def task_func(text1, text2):
    # Clean the texts by removing non-alphanumeric characters except spaces and converting to lowercase
    text1 = ALPHANUMERIC.sub('', text1).lower()
    text2 = ALPHANUMERIC.sub('', text2).lower()
    
    # Tokenize the texts
    words1 = text1.split()
    words2 = text2.split()
    
    # Create term frequency vectors
    term_freq1 = Counter(words1)
    term_freq2 = Counter(words2)
    
    # Get the unique terms from both texts
    unique_terms = set(term_freq1.keys()).union(set(term_freq2.keys()))
    
    # Create vectors for cosine similarity
    vector1 = np.array([term_freq1.get(term, 0) for term in unique_terms])
    vector2 = np.array([term_freq2.get(term, 0) for term in unique_terms])
    
    # Calculate cosine similarity
    cosine_similarity = np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
    
    # Calculate Levenshtein ratio
    levenshtein_ratio = ratio(text1, text2)
    
    return (cosine_similarity, levenshtein_ratio)