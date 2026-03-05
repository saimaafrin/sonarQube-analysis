import numpy as np
import pandas as pd
def task_func(n_rows, remove_cols, columns=['A', 'B', 'C', 'D', 'E'], random_seed=None):
    """
    Generates a DataFrame with specified number of rows and columns filled with random integers.
    Removes specified columns based on the provided indexes.

    Parameters:
    n_rows (int): Number of rows in the DataFrame.
    remove_cols (list): List of column indexes to be removed.
    columns (list): List of column names.
    random_seed (int): Seed for the random number generator for reproducibility.

    Returns:
    pd.DataFrame: The resulting DataFrame after removal of columns.
    """
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Create a DataFrame with random integers
    data = {col: np.random.randint(0, 101, n_rows) for col in columns}
    df = pd.DataFrame(data)
    
    # Remove specified columns
    df = df.drop(columns=[columns[i] for i in remove_cols])
    
    return df