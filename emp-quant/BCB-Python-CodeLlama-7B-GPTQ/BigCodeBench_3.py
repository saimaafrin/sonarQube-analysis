import random
import numpy as np
def task_func(LETTERS):
    """
    Create a dictionary where keys are specified letters and values are lists of random integers.
    Then calculate the mean of these integers for each key and return a dictionary of these means.
    """
    # Create a dictionary with letters as keys and lists of random integers as values
    letter_dict = {letter: [random.randint(0, 100) for _ in range(random.randint(1, 10))] for letter in LETTERS}

    # Calculate the mean of each list of integers
    mean_dict = {letter: np.mean(values) for letter, values in letter_dict.items()}

    return mean_dict
LETTERS = ['A', 'B', 'C', 'D', 'E']