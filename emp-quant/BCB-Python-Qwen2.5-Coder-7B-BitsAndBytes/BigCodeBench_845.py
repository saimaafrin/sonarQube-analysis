
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
    words1 = set(text1.split())
    words2 = set(text2.split())

    # Create word count vectors
    vector1 = np.zeros(len(words1))
    vector2 = np.zeros(len(words2))

    for i, word in enumerate(words1):
        if word in words2:
            vector1[i] += 1
            vector2[words2.index(word)] += 1

    # Normalize the vectors
    norm1 = np.linalg.norm(vector1)
    norm2 = np.linalg.norm(vector2)

    # Calculate cosine similarity
    cosine_similarity = np.dot(vector1, vector2) / (norm1 * norm2) if norm1 != 0 and norm2 != 0 else 0

    # Calculate Levenshtein ratio
    levenshtein_ratio = ratio(text1, text2)

    return (cosine_similarity, levenshtein_ratio)