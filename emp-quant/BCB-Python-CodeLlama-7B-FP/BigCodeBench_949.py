import numpy as np
import pandas as pd
import pytest
def task_func(rows, columns, seed=None):
    """
    Generate a DataFrame with random values within a specified range.

    This function creates a matrix of given dimensions filled with random values between 0 and 1 and returns it as a Pandas DataFrame.
    Users have the option to set a random seed for reproducible results.

    Parameters
    ----------
    rows : int
        The number of rows in the DataFrame.
    columns : int
        The number of columns in the DataFrame.
    seed : int, optional
        The random seed to use for reproducible results.

    Returns
    -------
    DataFrame
        A Pandas DataFrame containing the generated random values.
    """
    np.random.seed(seed)
    data = np.random.rand(rows, columns)
    return pd.DataFrame(data)