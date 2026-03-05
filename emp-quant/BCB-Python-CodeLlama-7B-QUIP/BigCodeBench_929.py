
import numpy as np
from scipy import stats

def task_func(word: str) -> np.ndarray:
    # Calculate the difference between the ASCII values of each pair of adjacent letters in the word
    differences = np.diff(word.encode())

    # Calculate the entropy of the differences
    entropy = stats.entropy(differences)

    return differences, entropy