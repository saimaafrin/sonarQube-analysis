import pandas as pd
import seaborn as sns
import numpy as np
import pytest
def task_func(data):
    """
    Creates and returns a heatmap of the cumulative sum of each column in a dictionary.
    """
    # Check if the DataFrame is empty
    if data.empty:
        raise ValueError("DataFrame is empty")

    # Check if there are any numeric columns
    if not data.select_dtypes(include=[np.number]).columns.size:
        raise ValueError("No numeric columns present")

    # Create a DataFrame with the cumulative sum of each column
    cumulative_sum = data.cumsum()

    # Create a Seaborn heatmap of the DataFrame
    ax = sns.heatmap(cumulative_sum, annot=True, cmap="YlGnBu")

    return ax