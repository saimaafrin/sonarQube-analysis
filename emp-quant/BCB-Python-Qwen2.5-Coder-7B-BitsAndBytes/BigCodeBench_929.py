
import numpy as np
from scipy import stats

def task_func(word: str) -> np.ndarray:
    # Calculate the difference between ASCII values of each pair of adjacent letters
    ascii_diffs = np.array([ord(word[i+1]) - ord(word[i]) for i in range(len(word)-1)])
    
    # Calculate the entropy of the differences
    probabilities = np.bincount(ascii_diffs + 128) / len(ascii_diffs)  # Adding 128 to handle negative values
    entropy = stats.entropy(probabilities)
    
    return ascii_diffs, entropy