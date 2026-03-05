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
    if not all(dataframe.dtypes == "float64"):
        raise TypeError("The DataFrame contains non-numeric columns.")

    # Check if the DataFrame has fewer than two columns
    if len(dataframe.columns) < 2:
        raise ValueError("The DataFrame has fewer than two columns.")

    # Calculate the correlation matrix
    correlation_matrix = dataframe.corr()

    # Find the pair of columns with the highest absolute correlation
    max_correlation = np.max(correlation_matrix.abs())
    max_correlation_index = np.argmax(correlation_matrix.abs())
    max_correlation_columns = correlation_matrix.columns[max_correlation_index]

    # Plot the scatter plot
    fig, ax = plt.subplots()
    ax.scatter(dataframe[max_correlation_columns[0]], dataframe[max_correlation_columns[1]])
    ax.set_xlabel(max_correlation_columns[0])
    ax.set_ylabel(max_correlation_columns[1])
    ax.set_title(f"Scatter Plot of {max_correlation_columns[0]} and {max_correlation_columns[1]}")

    return ax
dataframe = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [6, 7, 8, 9, 10]})