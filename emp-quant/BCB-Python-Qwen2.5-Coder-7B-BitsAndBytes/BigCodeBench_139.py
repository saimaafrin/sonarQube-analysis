
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

    # Check if the input is a non-empty DataFrame
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame.")

    # Filter out non-numeric columns
    numeric_columns = df.select_dtypes(include=[np.number]).columns

    # Raise an error if there are no numeric columns
    if len(numeric_columns) == 0:
        raise ValueError("DataFrame contains no numeric columns.")

    # Create a list to hold the axes objects
    axes_list = []

    # Plot histograms for each numeric column
    for col in numeric_columns:
        ax = df[col].hist(bins=30, figsize=(8, 6))
        ax.set_title(col)
        ax.set_xlabel('Value')
        ax.set_ylabel('Frequency')
        axes_list.append(ax)

    return axes_list