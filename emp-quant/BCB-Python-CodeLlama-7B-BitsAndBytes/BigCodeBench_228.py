
import pandas as pd
import numpy as np

# Constants
COLUMNS = ['column1', 'column2', 'column3', 'column4', 'column5']

def task_func(df, dct):
    # Check if input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")

    # Replace values in DataFrame with dictionary mapping
    for col in COLUMNS:
        df[col] = df[col].map(dct)

    # Calculate Pearson correlation coefficient between each pair of columns
    corr_matrix = df.corr(method='pearson')

    # Return correlation matrix as a DataFrame
    return corr_matrix

print(task_func(df, dct))