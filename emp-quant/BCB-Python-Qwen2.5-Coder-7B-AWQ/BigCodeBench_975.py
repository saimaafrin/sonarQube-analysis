import numpy as np
import pandas as pd
def task_func(rows, columns=["A", "B", "C", "D", "E"], seed=0) -> pd.DataFrame:
    """
    Create a Pandas DataFrame with a specified number of rows filled with random values in [0, 1) and shuffled columns.
    
    Parameters:
    rows (int): The number of rows in the DataFrame.
    columns (list): A list of column names. Defaults to ["A", "B", "C", "D", "E"].
    seed (int): The seed for the random number generator. Defaults to 0.
    
    Returns:
    pd.DataFrame: A pandas DataFrame with shuffled columns.
    """
    # Set the seed for the random number generator
    np.random.seed(seed)
    
    # Create a DataFrame with random values
    data = np.random.rand(rows, len(columns))
    df = pd.DataFrame(data, columns=columns)
    
    # Shuffle the columns
    df = df[columns[np.random.permutation(len(columns))]]
    
    return df