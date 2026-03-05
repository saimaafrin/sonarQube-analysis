import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(n_rows, scale_cols, columns=['A', 'B', 'C', 'D', 'E'], random_seed=None):
    """
    Generates a DataFrame with specified number of rows and columns, fills them with random values,
    and scales the columns at the provided indexes with sklearn StandardScaler.
    
    Parameters:
    - n_rows: int, the number of rows in the DataFrame.
    - scale_cols: list, the indexes of columns to be scaled.
    - columns: list, the names of the columns in the DataFrame.
    - random_seed: int, the seed for the random number generator for reproducibility.
    
    Returns:
    - DataFrame: The resulting DataFrame after scaling the selected columns.
    """
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate random data
    data = np.random.rand(n_rows, len(columns))
    df = pd.DataFrame(data, columns=columns)
    
    # Scale specified columns
    if scale_cols:
        scaler = StandardScaler()
        df.iloc[:, scale_cols] = scaler.fit_transform(df.iloc[:, scale_cols])
    
    return df