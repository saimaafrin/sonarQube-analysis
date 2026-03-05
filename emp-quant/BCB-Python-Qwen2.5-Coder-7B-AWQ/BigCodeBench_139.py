import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(df):
    """
    Draws histograms of numeric columns in a DataFrame and returns the plots.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame containing numeric columns.
    
    Returns:
    list: A list of Matplotlib Axes objects, each representing a histogram for a numeric column.
    
    Raises:
    ValueError: If the input is not a non-empty DataFrame or if there are no numeric columns in the DataFrame.
    """
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame.")
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if numeric_cols.empty:
        raise ValueError("No numeric columns found in the DataFrame.")
    
    axes = []
    for col in numeric_cols:
        ax = df[col].hist(bins=30, color='blue', edgecolor='black')
        ax.set_title(col)
        ax.set_xlabel('Value')
        ax.set_ylabel('Frequency')
        axes.append(ax)
    
    return axes