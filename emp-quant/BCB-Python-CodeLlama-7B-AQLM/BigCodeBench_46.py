from scipy.stats import zscore
import matplotlib.pyplot as plt
def task_func(df):
    """
    Calculate Z-scores for numeric columns in a DataFrame and draw a histogram for each column.
    - Missing values are replaced by the column's average.
    - The histograms are plotted with 10 bins.

    Parameters:
    - df (pandas.DataFrame): The input pandas DataFrame with numeric columns.

    Returns:
    - tuple:
        1. pandas.DataFrame: A DataFrame with computed z-scores.
        2. list: A list of Axes objects representing the histograms of the numeric columns.

    Requirements:
    - pandas.
    - numpy.
    - scipy.stats.zscore.
    - matplotlib.pyplot.

    Example:
    >>> import pandas as pd
    >>> import numpy as np
    >>> df_input = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7.0, np.nan, 9.0]], columns=["col1", "col2", "col3"])
    >>> zscore_output, plots = task_func(df_input)
    """
    # Replace missing values by the column's average.
    df = df.fillna(df.mean())

    # Calculate z-scores.
    zscores = zscore(df)

    # Draw histograms.
    plots = []
    for col in df.columns:
        plt.hist(zscores[col], bins=10)
        plots.append(plt.gca())

    # Return z-scores and plots.
    return zscores, plots