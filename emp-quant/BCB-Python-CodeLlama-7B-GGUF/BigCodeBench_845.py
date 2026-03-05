
import re
import numpy as np
from collections import Counter
from Levenshtein import ratio

# Constants
ALPHANUMERIC = re.compile('[\W_]+')

def task_func(text1, text2):
    # Clean the text by removing all non-alphanumeric characters except spaces
    text1 = re.sub(ALPHANUMERIC, '', text1.lower())
    text2 = re.sub(ALPHANUMERIC, '', text2.lower())

    # Compute the term frequency for each text
    term_freq1 = Counter(text1.split())
    term_freq2 = Counter(text2.split())

    # Compute the cosine similarity
    cosine_sim = np.dot(term_freq1, term_freq2) / (np.linalg.norm(term_freq1) * np.linalg.norm(term_freq2))

    # Compute the Levenshtein ratio
    levenshtein_ratio = ratio(text1, text2)

    return cosine_sim, levenshtein_ratio

cosine_sim, levenshtein_ratio = task_func(text1, text2)

print(f"Cosine similarity: {cosine_sim}")
print(f"Levenshtein ratio: {levenshtein_ratio}")