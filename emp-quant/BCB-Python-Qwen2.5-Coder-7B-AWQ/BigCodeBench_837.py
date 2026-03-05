import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(n_rows, scale_cols, columns=['A', 'B', 'C', 'D', 'E'], random_seed=None):
    """
    Generates a DataFrame with specified number of rows and columns, fills them with random values,
    and scales the specified columns using StandardScaler.
    
    Parameters:
    n_rows (int): Number of rows in the DataFrame.
    scale_cols (list): List of column indices to be scaled.
    columns (list): List of column names.
    random_seed (int): Seed for random number generator for reproducibility.
    
    Returns:
    pd.DataFrame: The resulting DataFrame after scaling the selected columns.
    """
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate random data
    data = {col: np.random.randn(n_rows) for col in columns}
    df = pd.DataFrame(data)
    
    # Scale specified columns
    if scale_cols:
        scaler = StandardScaler()
        df.iloc[:, scale_cols] = scaler.fit_transform(df.iloc[:, scale_cols])
    
    return df