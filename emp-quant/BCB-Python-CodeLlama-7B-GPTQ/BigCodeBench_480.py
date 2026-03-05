import re
import random
import pandas as pd
def task_func(data_list, seed=None):
    """
    Shuffle the substrings within each string in a given list.
    This function takes a list of comma-separated strings and splits each into substrings.
    It extracts substrings based on commas, removing leading and trailing whitespaces from each.
    Then, it shuffles these processed substrings within each string, and returns a pandas DataFrame with two columns: "Original String" and "Shuffled String".
    """
    # Split each string into substrings based on commas
    substrings = [re.split(r',\s*', s) for s in data_list]

    # Remove leading and trailing whitespaces from each substring
    substrings = [[s.strip() for s in ss] for ss in substrings]

    # Shuffle each substring within each string
    shuffled_substrings = [[random.sample(ss, k=len(ss)) for ss in substrings] for substrings in substrings]

    # Create a pandas DataFrame with two columns: "Original String" and "Shuffled String"
    df = pd.DataFrame({
        'Original String': data_list,
        'Shuffled String': shuffled_substrings
    })

    return df
data_list = ['a,b,c', 'd,e,f', 'g,h,i']