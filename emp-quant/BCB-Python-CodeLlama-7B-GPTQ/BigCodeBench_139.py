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
    # Check if the input is a non-empty DataFrame
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame")

    # Check if there are any numeric columns in the DataFrame
    if not df.select_dtypes(include=np.number).shape[1]:
        raise ValueError("DataFrame must have at least one numeric column")

    # Create a list to store the Matplotlib Axes objects
    ax_list = []

    # Iterate over the numeric columns in the DataFrame
    for col in df.select_dtypes(include=np.number).columns:
        # Create a histogram for each numeric column
        ax = df[col].plot.hist(title=col, xlabel="Value", ylabel="Frequency")
        ax_list.append(ax)

    # Return the list of Matplotlib Axes objects
    return ax_list
df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [6, 7, 8, 9, 10], "C": [11, 12, 13, 14, 15]})