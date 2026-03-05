
import collections
import random

# Constants
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

def task_func(n_keys, n_values):
    # Create a dictionary with random keys from LETTERS and values as lists of integers
    result_dict = {random.choice(LETTERS): list(range(1, n_values + 1)) for _ in range(n_keys)}
    return result_dict