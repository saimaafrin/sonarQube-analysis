
import re
import random
import pandas as pd

def task_func(data_list, seed=None):
    """
    Shuffle the substrings within each string in a given list.

    Parameters
    ----------
    data_list : list
        List of comma-separated strings.
    seed : int, optional
        Random seed for reproducibility.

    Returns
    -------
    DataFrame
        A pandas DataFrame with columns 'Original String' and 'Shuffled String'.
    """
    if seed is not None:
        random.seed(seed)

    # Split each string into substrings based on commas
    substrings = [re.split(r',\s*', s) for s in data_list]

    # Remove leading and trailing whitespaces from each substring
    substrings = [[s.strip() for s in ss] for ss in substrings]

    # Shuffle each list of substrings
    shuffled_substrings = [random.sample(ss, len(ss)) for ss in substrings]

    # Join the shuffled substrings back into strings
    shuffled_strings = [', '.join(ss) for ss in shuffled_substrings]

    # Create a DataFrame with the original and shuffled strings
    df = pd.DataFrame({'Original String': data_list, 'Shuffled String': shuffled_strings})

    return df