
import random
import numpy as np

def task_func(letters):
    """
    Create a dictionary where keys are specified letters and values are lists of random integers.
    Then calculate the mean of these integers for each key and return a dictionary of these means.
    """
    # Create a dictionary with keys as letters and values as lists of random integers
    data = {letter: random.sample(range(101), random.randint(1, 10)) for letter in letters}

    # Calculate the mean of each list of integers
    means = {letter: np.mean(integers) for letter, integers in data.items()}

    return means