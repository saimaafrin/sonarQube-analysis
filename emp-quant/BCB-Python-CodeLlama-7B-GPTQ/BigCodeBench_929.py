import numpy as np
from scipy import stats
def task_func(word: str) -> np.ndarray:
    """
    Calculate the difference between the ASCII values of each pair of adjacent letters in the input word.
    After calculating the difference, calculate the entropy of the differences.
    """
    # Calculate the difference between the ASCII values of each pair of adjacent letters
    differences = np.array([ord(word[i+1]) - ord(word[i]) for i in range(len(word)-1)])

    # Calculate the entropy of the differences
    entropy = stats.entropy(differences)

    return differences, entropy
word = "hello"