
import pandas as pd
import re
import random

def task_func(data_list, seed=None):
    # Set the random seed if provided
    if seed is not None:
        random.seed(seed)

    # Create a list of tuples containing the original and modified strings
    data = [(original, modified) for original in data_list for modified in [original.replace(",", "")]]

    # Create a pandas DataFrame from the list of tuples
    df = pd.DataFrame(data, columns=["Original String", "Modified String"])

    return df