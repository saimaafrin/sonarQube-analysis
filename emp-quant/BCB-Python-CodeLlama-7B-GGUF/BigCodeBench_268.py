
import collections
import random

# Constants
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

def task_func(n_keys, n_values):
    """
    Create a Python dictionary with a specified number of keys and values.
    Keys are randomly selected from a predefined list of letters, and values are consecutive integers starting from 1.
    Due to the randomness in key selection, the actual keys in the dictionary may vary in each execution.
    """
    # Create a dictionary to store the keys and values
    key_value_dict = collections.defaultdict(list)

    # Generate random keys
    random_keys = random.sample(LETTERS, n_keys)

    # Generate consecutive values
    values = list(range(1, n_values + 1))

    # Add keys and values to the dictionary
    for key in random_keys:
        key_value_dict[key].extend(values)

    return key_value_dict