
import pandas as pd
import numpy as np

# Constants
COLUMNS = ['column1', 'column2', 'column3', 'column4', 'column5']

def task_func(df, dct):
    """
    Replace certain values in a DataFrame with a dictionary mapping and calculate the Pearson correlation coefficient between each pair of columns.

    Parameters:
    df (pd.DataFrame): Input DataFrame
    dct (dict): Dictionary mapping values to replace

    Returns:
    pd.DataFrame: A DataFrame with the correlation coefficients between each pair of columns. The format of the DataFrame is a square matrix with column and index labels matching the columns of the input DataFrame.

    Raises:
    ValueError: If input df is not a DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df must be a DataFrame")

    # Replace values in the DataFrame using the dictionary mapping
    df = df.replace(dct)

    # Calculate the correlation coefficient between each pair of columns
    corr_matrix = df.corr()

    return corr_matrix

dct = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}

corr_matrix = task_func(df, dct)

print(corr_matrix)