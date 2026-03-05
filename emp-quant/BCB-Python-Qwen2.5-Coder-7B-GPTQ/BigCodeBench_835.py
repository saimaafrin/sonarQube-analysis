import numpy as np
import pandas as pd
def task_func(n_rows, remove_cols, columns=['A', 'B', 'C', 'D', 'E'], random_seed=None):
    """
    Generates a DataFrame with specified number of rows and columns, fills it with random integers,
    and removes specified columns.

    :param n_rows: Number of rows in the DataFrame
    :param remove_cols: List of column indices to remove
    :param columns: List of column names
    :param random_seed: Seed for random number generator for reproducibility
    :return: DataFrame after removing specified columns
    """
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate random data
    data = np.random.randint(0, 101, size=(n_rows, len(columns)))
    
    # Create DataFrame
    df = pd.DataFrame(data, columns=columns)
    
    # Remove specified columns
    df = df.drop(columns=[columns[i] for i in remove_cols])
    
    return df