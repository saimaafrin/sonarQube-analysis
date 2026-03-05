
import collections
import random

# Constants
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

def task_func(n_keys, n_values):
    # Create a dictionary with random keys from the LETTERS list
    keys = random.sample(LETTERS, n_keys)
    # Create a dictionary with keys and values
    result_dict = {key: list(range(1, n_values + 1)) for key in keys}
    return result_dict