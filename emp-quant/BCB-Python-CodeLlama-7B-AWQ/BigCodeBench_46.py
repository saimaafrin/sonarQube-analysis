import pandas as pd
import numpy as np
from scipy.stats import zscore
import matplotlib.pyplot as plt
def task_func(df):
    """
    Calculate Z-scores for numeric columns in a DataFrame and draw a histogram for each column.
    Missing values are replaced by the column's average.
    The histograms are plotted with 10 bins.
    """
    # Replace missing values with column average
    df = df.fillna(df.mean())

    # Calculate Z-scores
    zscores = zscore(df)

    # Create a list of Axes objects to store the histograms
    ax_list = []

    # Iterate over numeric columns
    for col in df.select_dtypes(include=['number']).columns:
        # Calculate histogram
        ax = df[col].hist(bins=10)
        ax_list.append(ax)

    # Return a tuple of the DataFrame with computed Z-scores and the list of Axes objects
    return zscores, ax_list
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50], 'C': [100, 200, 300, 400, 500]})