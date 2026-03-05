
import pandas as pd
import numpy as np

# Constants
COLUMNS = ['column1', 'column2', 'column3', 'column4', 'column5']

def task_func(df, dct):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df is not a DataFrame")
    
    # Replace certain values in the DataFrame with the dictionary mapping
    df = df.replace(dct)
    
    # Calculate the Pearson correlation coefficient between each pair of columns
    correlation_matrix = df.corr(method='pearson')
    
    return correlation_matrix