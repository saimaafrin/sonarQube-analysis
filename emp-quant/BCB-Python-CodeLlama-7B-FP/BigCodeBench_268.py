import collections
import random
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
def task_func(n_keys, n_values):
    """
    Create a Python dictionary with a specified number of keys and values.
    Keys are randomly selected from a predefined list of letters, and values are consecutive integers starting from 1.
    Due to the randomness in key selection, the actual keys in the dictionary may vary in each execution.
    """
    # Create a dictionary to store the keys and values
    result = collections.defaultdict(list)

    # Generate random keys and values
    for i in range(n_keys):
        key = random.choice(LETTERS)
        value = i + 1
        result[key].append(value)

    return result