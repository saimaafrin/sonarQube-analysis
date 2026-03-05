
import numpy as np
from scipy import stats

def task_func(word: str) -> np.ndarray:
    # Calculate the difference between ASCII values of each pair of adjacent letters
    ascii_diffs = np.array([ord(word[i+1]) - ord(word[i]) for i in range(len(word)-1)])
    
    # Calculate the entropy of the differences
    entropy = stats.entropy(np.bincount(ascii_diffs), base=2)
    
    return ascii_diffs, entropy