import seaborn as sns
import numpy as np
import pandas as pd
import pytest
def task_func(df):
    """
    Generates a pair plot from a numeric DataFrame and calculates its covariance matrix.

    Args:
        df (pandas.DataFrame): The input DataFrame.

    Returns:
        tuple:
        covariance_df (pandas.DataFrame): The covariance matrix of the input DataFrame.
        pair_plot (sns.axisgrid.PairGrid): Pair plot of the input DataFrame.

    Raises:
        ValueError: If the DataFrame is empty.
        TypeError: If the DataFrame contains non-numeric data types.
    """
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The DataFrame is empty.")

    # Check if the DataFrame contains non-numeric data types
    if not all(df.dtypes == np.number):
        raise TypeError("The DataFrame contains non-numeric data types.")

    # Calculate the covariance matrix
    covariance_df = df.cov()

    # Generate the pair plot
    pair_plot = sns.pairplot(df)

    return covariance_df, pair_plot