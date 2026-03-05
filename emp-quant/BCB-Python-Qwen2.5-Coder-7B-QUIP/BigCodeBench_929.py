
import numpy as np
from scipy import stats

def task_func(word: str) -> np.ndarray:
    # Calculate the difference between the ASCII values of each pair of adjacent letters
    ascii_diffs = [ord(word[i + 1]) - ord(word[i]) for i in range(len(word) - 1)]
    
    # Convert the list of differences to a numpy array
    ascii_diffs_array = np.array(ascii_diffs)
    
    # Calculate the entropy of the differences
    entropy = stats.entropy(ascii_diffs_array)
    
    return ascii_diffs_array, entropy