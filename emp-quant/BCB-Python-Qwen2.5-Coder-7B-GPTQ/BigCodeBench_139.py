import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(df):
    # Check if the input is a non-empty DataFrame
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame")
    
    # Check if there are any numeric columns in the DataFrame
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if numeric_cols.empty:
        raise ValueError("DataFrame must contain at least one numeric column")
    
    # Create a list to hold the Axes objects
    axes = []
    
    # Loop through each numeric column and create a histogram
    for col in numeric_cols:
        ax = df[col].hist(bins=10, edgecolor='black')
        ax.set_title(col)
        ax.set_xlabel('Value')
        ax.set_ylabel('Frequency')
        axes.append(ax)
    
    return axes