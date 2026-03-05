
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(df):
    # Check if the input is a non-empty DataFrame
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame")
    
    # Check if there are any numeric columns in the DataFrame
    numeric_columns = df.select_dtypes(include=['number']).columns
    if not numeric_columns:
        raise ValueError("No numeric columns found in the DataFrame")
    
    # Initialize a list to store the Axes objects
    axes = []
    
    # Create histograms for each numeric column
    for column in numeric_columns:
        fig, ax = plt.subplots()
        df[column].hist(ax=ax, bins=10, color='blue')
        ax.set_title(column)
        ax.set_xlabel('Value')
        ax.set_ylabel('Frequency')
        axes.append(ax)
    
    return axes