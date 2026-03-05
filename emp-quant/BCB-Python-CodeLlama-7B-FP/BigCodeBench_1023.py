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
    ax : matplotlib.pyplot.Axes
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
    if not dataframe.select_dtypes(include=[np.number]).empty:
        raise TypeError("The DataFrame contains non-numeric columns.")

    # Check if the DataFrame has fewer than two columns
    if len(dataframe.columns) < 2:
        raise ValueError("The DataFrame has fewer than two columns.")

    # Calculate the correlation matrix
    corr = dataframe.corr()

    # Find the pair of columns with the highest absolute correlation
    max_corr = corr.max().max()
    max_corr_cols = corr.columns[corr.max() == max_corr]

    # Plot the scatter plot
    fig, ax = plt.subplots()
    ax.scatter(dataframe[max_corr_cols[0]], dataframe[max_corr_cols[1]])
    ax.set_xlabel(max_corr_cols[0])
    ax.set_ylabel(max_corr_cols[1])
    ax.set_title(f"Scatter Plot of {max_corr_cols[0]} and {max_corr_cols[1]}")

    return ax
dataframe = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [2, 4, 6, 8, 10]})