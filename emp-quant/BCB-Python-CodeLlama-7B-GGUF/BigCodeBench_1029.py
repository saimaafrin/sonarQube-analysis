
import pandas as pd
import numpy as np

def task_func(rows=100, columns=3):
    """
    Create a Pandas DataFrame with random alphabets.

    Parameters
    ----------
    rows : int, optional
        Number of rows in the DataFrame. Default is 100.
    columns : int, optional
        Number of columns in the DataFrame. Default is 3.

    Returns
    -------
    DataFrame : pandas.DataFrame
        A Pandas DataFrame with random alphabets.
    """
    # Create a list of random alphabets
    alphabet = np.random.choice(list('abcdefghijklmnopqrstuvwxyz'), size=(rows, columns))

    # Create a DataFrame from the list
    df = pd.DataFrame(alphabet, columns=['a', 'b', 'c'])

    return df