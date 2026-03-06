
import numpy as np
from itertools import product
import string

def task_func(length, seed=None, alphabets=list(string.ascii_lowercase)):
    """
    Generate a list of randomly picked strings from all possible strings of a given length from the provided series of characters, using a specific seed for reproducibility.

    Args:
        length (int): The length of the strings to generate.
        seed (int, optional): The seed to use for reproducibility. Defaults to None.
        alphabets (list, optional): The series of characters to use for generating the strings. Defaults to list(string.ascii_lowercase).

    Returns:
        list: A list of generated strings.
    """
    np.random.seed(seed)
    all_strings = [*product(alphabets, repeat=length)]
    return np.random.choice(all_strings, size=10, replace=False).tolist()