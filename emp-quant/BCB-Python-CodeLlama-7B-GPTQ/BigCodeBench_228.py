import pandas as pd
import numpy as np
def task_func(df, dct):
    """
    Replace certain values in a DataFrame with a dictionary mapping and calculate the Pearson correlation coefficient between each pair of columns.
    """
    # Check if input df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df must be a DataFrame")

    # Replace values in df with dictionary mapping
    df = df.replace(dct)

    # Calculate Pearson correlation coefficient between each pair of columns
    corr_matrix = df.corr(method='pearson')

    # Return correlation matrix as a DataFrame
    return corr_matrix
df = pd.DataFrame({
    'column1': [1, 2, 3, 4, 5],
    'column2': [2, 4, 6, 8, 10],
    'column3': [3, 6, 9, 12, 15],
    'column4': [4, 8, 12, 16, 20],
    'column5': [5, 10, 15, 20, 25]
})
dct = {
    'column1': {1: 10, 2: 20, 3: 30},
    'column2': {4: 40, 6: 60, 9: 90},
    'column3': {12: 120, 15: 150, 18: 180},
    'column4': {16: 160, 20: 200, 24: 240},
    'column5': {25: 250, 30: 300, 35: 350}
}