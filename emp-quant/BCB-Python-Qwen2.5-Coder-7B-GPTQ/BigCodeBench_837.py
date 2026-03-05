import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(n_rows, scale_cols, columns=['A', 'B', 'C', 'D', 'E'], random_seed=None):
    """
    Generates a DataFrame with specified number of rows and columns, fills them with random values,
    and scales the specified columns using StandardScaler.
    
    :param n_rows: Number of rows in the DataFrame
    :param scale_cols: List of column indices to scale
    :param columns: List of column names
    :param random_seed: Seed for random number generator for reproducibility
    :return: DataFrame with scaled columns
    """
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate random data
    data = np.random.rand(n_rows, len(columns))
    df = pd.DataFrame(data, columns=columns)
    
    # Scale specified columns
    scaler = StandardScaler()
    if scale_cols:
        df.iloc[:, scale_cols] = scaler.fit_transform(df.iloc[:, scale_cols])
    
    return df