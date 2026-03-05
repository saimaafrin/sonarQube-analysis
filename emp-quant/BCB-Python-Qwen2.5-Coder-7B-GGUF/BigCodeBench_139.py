
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(df):
    # Check if the input is a non-empty DataFrame
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame")
    
    # Check if there are any numeric columns in the DataFrame
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    if numeric_columns.empty:
        raise ValueError("DataFrame must contain at least one numeric column")
    
    # Create a list to hold the Axes objects
    axes = []
    
    # Loop through each numeric column and create a histogram
    for column in numeric_columns:
        ax = df[column].hist(bins=20, edgecolor='black')
        ax.set_title(column)
        ax.set_xlabel('Value')
        ax.set_ylabel('Frequency')
        axes.append(ax)
    
    return axes