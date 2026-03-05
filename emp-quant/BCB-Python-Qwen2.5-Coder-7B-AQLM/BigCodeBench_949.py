
import numpy as np
import pandas as pd

def task_func(rows, columns, seed=None):
    """
    Generates a DataFrame with random values within a specified range.

    Parameters:
    rows (int): The number of rows in the DataFrame.
    columns (int): The number of columns in the DataFrame.
    seed (int, optional): A random seed for reproducible results. Defaults to None.

    Returns:
    DataFrame: A Pandas DataFrame containing the generated random values.
    """
    if seed is not None:
        np.random.seed(seed)
    
    random_matrix = np.random.rand(rows, columns)
    df = pd.DataFrame(random_matrix)
    return df