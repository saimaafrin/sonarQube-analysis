
import re
import numpy as np
from collections import Counter
from Levenshtein import ratio

# Constants
ALPHANUMERIC = re.compile('[\W_]+')

def task_func(text1, text2):
    # Clean the texts
    text1 = re.sub(ALPHANUMERIC, '', text1).lower()
    text2 = re.sub(ALPHANUMERIC, '', text2).lower()

    # Tokenize the texts
    tokens1 = text1.split()
    tokens2 = text2.split()

    # Create term frequency vectors
    all_tokens = tokens1 + tokens2
    all_tokens = set(all_tokens)
    term_freq1 = [tokens1.count(token) for token in all_tokens]
    term_freq2 = [tokens2.count(token) for token in all_tokens]

    # Convert to numpy arrays
    term_freq1 = np.array(term_freq1)
    term_freq2 = np.array(term_freq2)

    # Calculate cosine similarity
    cosine_sim = np.dot(term_freq1, term_freq2) / (np.linalg.norm(term_freq1) * np.linalg.norm(term_freq2))

    # Calculate Levenshtein ratio
    levenshtein_ratio = ratio(text1, text2)

    return (cosine_sim, levenshtein_ratio)