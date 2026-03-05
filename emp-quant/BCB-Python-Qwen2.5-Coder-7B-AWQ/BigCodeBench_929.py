import numpy as np
from scipy import stats
def task_func(word: str) -> np.ndarray:
    # Calculate the difference between ASCII values of adjacent letters
    ascii_diffs = np.array([ord(word[i]) - ord(word[i-1]) for i in range(1, len(word))])
    
    # Calculate the entropy of the differences
    entropy = stats.entropy(np.bincount(ascii_diffs) / len(ascii_diffs), base=2)
    
    return ascii_diffs, entropy