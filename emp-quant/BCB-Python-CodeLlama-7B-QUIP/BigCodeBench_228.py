
import pandas as pd
import numpy as np

# Constants
COLUMNS = ['column1', 'column2', 'column3', 'column4', 'column5']

def task_func(df, dct):
    # Replace values in DataFrame with dictionary
    for col in df.columns:
        if col in dct:
            df[col] = df[col].replace(dct[col])

    # Calculate Pearson correlation coefficient between each pair of columns
    corr_df = df.corr(method='pearson')

    # Return correlation matrix
    return corr_df