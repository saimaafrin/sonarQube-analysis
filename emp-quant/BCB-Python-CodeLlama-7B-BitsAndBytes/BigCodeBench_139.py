
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(df):
    # Check if input is a non-empty DataFrame and if there are any numeric columns
    if not isinstance(df, pd.DataFrame) or df.empty or not df.select_dtypes(include=[np.number]).empty:
        raise ValueError("Input must be a non-empty DataFrame with numeric columns")

    # Create a list to store the Matplotlib Axes objects
    ax_list = []

    # Iterate over the numeric columns in the DataFrame
    for col in df.select_dtypes(include=[np.number]):
        # Create a histogram for each column
        ax = df[col].hist(bins=50, xlabel='Value', ylabel='Frequency', title=col)
        ax_list.append(ax)

    # Return the list of Matplotlib Axes objects
    return ax_list