
import numpy as np
from scipy import stats

def task_func(word: str) -> np.ndarray:
    # Calculate the ASCII values of each letter in the word
    ascii_values = [ord(letter) for letter in word]

    # Calculate the difference between each pair of adjacent letters
    differences = np.diff(ascii_values)

    # Calculate the entropy of the differences
    entropy = stats.entropy(differences)

    return differences, entropy