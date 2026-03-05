import pandas as pd
import numpy as np
def task_func(rows=100, columns=3):
    """
    Create a Pandas DataFrame with random alphabets in each cell.
    The DataFrame will have a specified number of rows and columns.
    Each column is named with a string from the list ['a', 'b', 'c', ...] depending on the number of columns specified.
    """
    # Create a list of random alphabets
    alphabets = np.random.choice(list('abcdefghijklmnopqrstuvwxyz'), size=rows)

    # Create a list of column names
    column_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # Create a Pandas DataFrame
    df = pd.DataFrame(data=alphabets, columns=column_names[:columns])

    return df