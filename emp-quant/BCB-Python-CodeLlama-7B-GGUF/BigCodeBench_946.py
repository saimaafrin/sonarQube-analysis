
import numpy as np
import pandas as pd
import random

def task_func(rows=3, cols=2, min_val=0, max_val=100, seed=0):
    """
    Creates a matrix of specified dimensions with random integers within a given range, and then converts it into a pandas DataFrame.

    Parameters
    ----------
    rows : int, optional
        Number of rows in the matrix. Default is 3.
    cols : int, optional
        Number of columns in the matrix. Default is 2.
    min_val : int, optional
        Minimum value in the random integer range. Default is 0.
    max_val : int, optional
        Maximum value in the random integer range. Default is 100.
    seed : int, optional
        Random seed for reproducibility. Default is 0.

    Returns
    -------
    DataFrame : pandas.DataFrame
        A pandas DataFrame containing random integers within the specified range.
    """
    # Set random seed for reproducibility
    random.seed(seed)

    # Create a matrix with random integers within the specified range
    matrix = np.random.randint(min_val, max_val, size=(rows, cols))

    # Convert the matrix to a pandas DataFrame
    df = pd.DataFrame(matrix)

    return df