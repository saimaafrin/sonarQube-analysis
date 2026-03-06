import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(dataframe):
    """
    Calculate the correlation matrix of a DataFrame and plot a scatter plot for the pair of columns with the highest absolute correlation.

    Parameters:
    - dataframe (pd.DataFrame): The DataFrame containing numeric columns for correlation calculation.

    Returns:
    - ax (plt.Axes): The scatter plot of the pair of columns with the highest absolute correlation.

    Requirements:
    - pandas
    - numpy
    - matplotlib

    Exception Handling:
    - Raises ValueError if the input DataFrame is empty.
    - Raises TypeError if any column in the DataFrame is non-numeric.
    - Raises ValueError if the DataFrame has fewer than two columns.

    Example:
    >>> df = pd.DataFrame({
    ...     'A': np.random.rand(100),
    ...     'B': np.random.rand(100),
    ...     'C': np.random.rand(100)
    ... })
    >>> ax = task_func(df)
    >>> print(ax)
    Axes(0.125,0.11;0.775x0.77)
    """
    if dataframe.empty:
        raise ValueError("The input DataFrame is empty.")
    if dataframe.dtypes.any() != np.dtype('float64'):
        raise TypeError("The input DataFrame contains non-numeric columns.")
    if len(dataframe.columns) < 2:
        raise ValueError("The input DataFrame has fewer than two columns.")

    corr = dataframe.corr()
    corr_abs = np.abs(corr)
    max_corr = np.max(corr_abs)
    max_corr_idx = np.where(corr_abs == max_corr)
    max_corr_col_idx = max_corr_idx[0][0]
    max_corr_row_idx = max_corr_idx[1][0]
    max_corr_col = corr.columns[max_corr_col_idx]
    max_corr_row = corr.index[max_corr_row_idx]
    ax = plt.scatter(dataframe[max_corr_col], dataframe[max_corr_row])
    return ax