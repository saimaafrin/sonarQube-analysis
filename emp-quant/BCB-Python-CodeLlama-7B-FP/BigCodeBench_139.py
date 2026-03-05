import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(df):
    """
    Draw histograms of numeric columns in a DataFrame and return the plots.
    Each histogram represents the distribution of values in one numeric column,
    with the column name as the plot title, 'Value' as the x-axis label, and
    'Frequency' as the y-axis label.
    """
    # Check if input is a non-empty DataFrame and if there are any numeric columns
    if not isinstance(df, pd.DataFrame) or not df.select_dtypes(include=[np.number]).shape[1]:
        raise ValueError("Input must be a non-empty DataFrame with numeric columns")

    # Create a list to store the Matplotlib Axes objects
    ax_list = []

    # Iterate over numeric columns and create a histogram for each
    for col in df.select_dtypes(include=[np.number]):
        # Create a histogram for the current column
        ax = df[col].hist(xlabel="Value", ylabel="Frequency", title=col)
        ax_list.append(ax)

    # Return the list of Matplotlib Axes objects
    return ax_list
df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [10, 20, 30, 40, 50], "C": [100, 200, 300, 400, 500]})