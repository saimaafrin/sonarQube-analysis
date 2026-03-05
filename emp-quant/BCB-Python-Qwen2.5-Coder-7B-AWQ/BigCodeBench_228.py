import pandas as pd
import numpy as np
def task_func(df, dct):
    """
    Replaces certain values in a DataFrame with a dictionary mapping and calculates the Pearson correlation coefficient between each pair of columns.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame.
    dct (dict): A dictionary mapping values to be replaced in the DataFrame.
    
    Returns:
    pd.DataFrame: A DataFrame with the correlation coefficients between each pair of columns.
    
    Raises:
    ValueError: If the input df is not a DataFrame.
    """
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df is not a DataFrame.")
    
    # Replace values in the DataFrame based on the dictionary mapping
    df_replaced = df.replace(dct)
    
    # Calculate the Pearson correlation coefficient between each pair of columns
    correlation_matrix = df_replaced.corr(method='pearson')
    
    return correlation_matrix