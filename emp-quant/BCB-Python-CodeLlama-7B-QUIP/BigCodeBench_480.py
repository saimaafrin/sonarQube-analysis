
import re
import random
import pandas as pd

def task_func(data_list, seed=None):
    # Initialize the random seed
    if seed:
        random.seed(seed)

    # Split the strings into substrings based on commas
    substrings = [re.split(r'\s*,\s*', s) for s in data_list]

    # Shuffle the substrings within each string
    shuffled_substrings = [random.sample(s, len(s)) for s in substrings]

    # Create a DataFrame with the original and shuffled strings
    df = pd.DataFrame({
        'Original String': data_list,
        'Shuffled String': shuffled_substrings
    })

    return df