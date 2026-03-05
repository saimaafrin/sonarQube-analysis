import numpy as np
import pandas as pd
import unittest
def task_func(rows, columns, seed=None):
    """
    Generate a DataFrame with random values within a specified range.
    This function creates a matrix of given dimensions filled with random values between 0 and 1 and returns it as a Pandas DataFrame.
    Users have the option to set a random seed for reproducible results.
    """
    if seed is not None:
        np.random.seed(seed)
    data = np.random.rand(rows, columns)
    return pd.DataFrame(data)