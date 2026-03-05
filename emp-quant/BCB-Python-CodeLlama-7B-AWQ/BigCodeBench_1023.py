import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(dataframe):
    """
    Calculate the correlation matrix of a DataFrame and plot a scatter plot for the pair of columns with the highest absolute correlation.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The input DataFrame.

    Returns
    -------
    ax : matplotlib.axes.Axes
        The scatter plot of the pair of columns with the highest absolute correlation.

    Raises
    ------
    ValueError
        If the input DataFrame is empty.
    TypeError
        If any column in the DataFrame is non-numeric.
    ValueError
        If the DataFrame has fewer than two columns.
    """
    # Check if the DataFrame is empty
    if dataframe.empty:
        raise ValueError("The input DataFrame is empty.")

    # Check if any column in the DataFrame is non-numeric
    if not all(dataframe.dtypes == "float64"):
        raise TypeError("The DataFrame contains non-numeric columns.")

    # Check if the DataFrame has fewer than two columns
    if len(dataframe.columns) < 2:
        raise ValueError("The DataFrame has fewer than two columns.")

    # Calculate the correlation matrix
    corr_matrix = dataframe.corr()

    # Find the pair of columns with the highest absolute correlation
    max_corr = corr_matrix.max().max()
    max_corr_cols = corr_matrix.columns[corr_matrix.max() == max_corr]

    # Plot the scatter plot
    ax = dataframe[max_corr_cols].plot.scatter(x=max_corr_cols[0], y=max_corr_cols[1])

    return ax
dataframe = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})