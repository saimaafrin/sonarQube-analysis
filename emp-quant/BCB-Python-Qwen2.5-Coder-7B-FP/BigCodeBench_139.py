import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(df):
    # Check if the input is a non-empty DataFrame
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame")
    
    # Check if there are any numeric columns in the DataFrame
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if not numeric_cols.empty:
        # Create a list to hold the Axes objects
        axes = []
        
        # Loop through each numeric column and create a histogram
        for col in numeric_cols:
            ax = df[col].hist(bins=10, figsize=(8, 6))
            ax.set_title(col)
            ax.set_xlabel('Value')
            ax.set_ylabel('Frequency')
            axes.append(ax)
        
        return axes
    else:
        raise ValueError("No numeric columns found in the DataFrame")
df = pd.DataFrame({
    'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7],
    'B': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    'C': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
})