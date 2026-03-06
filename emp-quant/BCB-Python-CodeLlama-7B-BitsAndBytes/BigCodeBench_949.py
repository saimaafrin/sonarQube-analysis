
import numpy as np
import pandas as pd

def task_func(rows, columns, seed=None):
    """
    Generate a DataFrame with random values within a specified range.

    Parameters
    ----------
    rows : int
        Number of rows in the DataFrame.
    columns : int
        Number of columns in the DataFrame.
    seed : int, optional
        Random seed for reproducible results.

    Returns
    -------
    DataFrame
        A Pandas DataFrame containing the generated random values.
    """
    np.random.seed(seed)
    data = np.random.rand(rows, columns)
    return pd.DataFrame(data)