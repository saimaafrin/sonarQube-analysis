
import pandas as pd
import numpy as np

def task_func(df, col):
    """
    Removes a specific column from the DataFrame and adds an 'IsEvenIndex' column.

    Parameters:
    df (pd.DataFrame): The input DataFrame to process.
    col (str): The name of the column to remove.

    Returns:
    pd.DataFrame: The processed DataFrame with the specified column removed and a new 'IsEvenIndex' column added.
    """
    # Remove the specified column
    df = df.drop(columns=[col])
    
    # Add 'IsEvenIndex' column
    df['IsEvenIndex'] = df.index % 2 == 0
    
    return df