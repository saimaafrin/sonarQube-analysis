
import pandas as pd
import numpy as np

# Constants
COLUMNS = ['column1', 'column2', 'column3', 'column4', 'column5']

def task_func(df, dct):
    """
    Replaces certain values in a DataFrame with a dictionary mapping and calculates the Pearson correlation coefficient between each pair of columns.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame.
    dct (dict): A dictionary mapping values to be replaced.
    
    Returns:
    pd.DataFrame: A DataFrame with the correlation coefficients between each pair of columns.
    
    Raises:
    ValueError: If the input df is not a DataFrame.
    """
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df is not a DataFrame.")
    
    # Replace values in the DataFrame based on the dictionary mapping
    for old_value, new_value in dct.items():
        df = df.replace(old_value, new_value)
    
    # Calculate the Pearson correlation coefficient between each pair of columns
    correlation_matrix = df.corr(method='pearson')
    
    return correlation_matrix

    # Define the dictionary mapping
    dct = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70}
    
    # Calculate the correlation matrix
    correlation_matrix = task_func(df, dct)
    
    # Print the correlation matrix
    print(correlation_matrix)