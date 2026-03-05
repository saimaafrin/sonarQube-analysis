
import pandas as pd
import re
import random

def task_func(data_list, seed=None):
    """
    Removes a random comma-separated value (treated as a "substring") from each string in a list and returns a pandas DataFrame containing the original and modified strings.
    """
    if seed is not None:
        random.seed(seed)

    # Create a list of tuples containing the original and modified strings
    data = [(original, re.sub(r',\w+', '', original)) for original in data_list]

    # Create a pandas DataFrame from the list of tuples
    df = pd.DataFrame(data, columns=['Original String', 'Modified String'])

    return df