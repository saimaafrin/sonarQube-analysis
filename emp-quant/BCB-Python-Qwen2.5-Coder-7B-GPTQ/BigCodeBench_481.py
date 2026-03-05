import pandas as pd
import random
import re
def task_func(data_list, seed=42):
    """
    Randomizes the order of comma-separated substrings within each string in a list,
    normalizes spaces to ensure a single space follows each comma, then returns a DataFrame
    comparing original and randomized strings.
    
    :param data_list: List of strings to process.
    :param seed: Seed for random number generator for reproducibility.
    :return: pandas.DataFrame with columns 'Original String' and 'Randomized String'.
    """
    random.seed(seed)
    result = []
    for item in data_list:
        # Normalize spaces and split by comma
        substrings = re.split(r'\s*,\s*', item)
        # Shuffle the substrings
        random.shuffle(substrings)
        # Join shuffled substrings with a single space
        randomized_item = ', '.join(substrings)
        result.append({'Original String': item, 'Randomized String': randomized_item})
    return pd.DataFrame(result)
data_list = [
    "apple, banana, cherry",
    "dog, cat, bird, fish",
    "red, green, blue, yellow"
]