
import re
import random
import pandas as pd

def task_func(data_list, seed=None):
    """
    Shuffle the substrings within each string in a given list.

    Parameters:
    data_list (list): A list of comma-separated strings.
    seed (int, optional): A random seed for reproducibility.

    Returns:
    DataFrame: A pandas DataFrame with columns 'Original String' and 'Shuffled String'.
    """
    # Split each string into substrings based on commas
    substrings = [re.split(r',\s*', s) for s in data_list]

    # Remove leading and trailing whitespaces from each substring
    substrings = [[s.strip() for s in ss] for ss in substrings]

    # Shuffle each substring within each string
    shuffled_substrings = [[random.sample(ss, len(ss)) for ss in ss] for ss in substrings]

    # Create a DataFrame with the original and shuffled strings
    df = pd.DataFrame({'Original String': data_list, 'Shuffled String': shuffled_substrings})

    return df