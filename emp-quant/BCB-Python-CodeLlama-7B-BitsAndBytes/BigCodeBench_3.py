
import random
import numpy as np

def task_func(LETTERS):
    # Create a dictionary with keys as letters and values as lists of random integers
    letter_dict = {letter: random.sample(range(101), 10) for letter in LETTERS}

    # Calculate the mean of each list of integers
    mean_dict = {letter: np.mean(values) for letter, values in letter_dict.items()}

    return mean_dict