import pandas as pd
import numpy as np
COLUMNS = ['column1', 'column2', 'column3', 'column4', 'column5']
def task_func(df, dct):
    """
    Replace certain values in a DataFrame with a dictionary mapping and calculate the Pearson correlation coefficient between each pair of columns.
    """
    # Check if input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")

    # Replace values in the DataFrame with the dictionary mapping
    for col in COLUMNS:
        df[col] = df[col].replace(dct)

    # Calculate the correlation matrix
    corr_matrix = df.corr(method='pearson')

    # Return the correlation matrix as a DataFrame
    return corr_matrix
df = pd.DataFrame({'column1': [1, 2, 3, 4, 5],
                   'column2': [2, 4, 6, 8, 10],
                   'column3': [3, 6, 9, 12, 15],
                   'column4': [4, 8, 12, 16, 20],
                   'column5': [5, 10, 15, 20, 25]})
dct = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}