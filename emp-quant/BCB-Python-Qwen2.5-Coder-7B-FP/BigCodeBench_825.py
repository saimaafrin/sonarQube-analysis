import numpy as np
from itertools import product
import string
def task_func(length, seed=None, alphabets=list(string.ascii_lowercase)):
    """
    Generate a list of 10 randomly picked strings from all possible strings of a given length from the provided series of characters, using a specific seed for reproducibility.

    Parameters:
    length (int): The length of the strings to generate.
    seed (int, optional): The seed for the random number generator for reproducibility. Defaults to None.
    alphabets (list, optional): The list of characters to use for generating the strings. Defaults to all lowercase English letters.

    Returns:
    list: A list of generated strings.
    """
    if seed is not None:
        np.random.seed(seed)
    
    # Generate all possible strings of the given length
    all_strings = [''.join(p) for p in product(alphabets, repeat=length)]
    
    # Randomly pick 10 strings from the list
    selected_strings = np.random.choice(all_strings, 10, replace=False)
    
    return selected_strings.tolist()