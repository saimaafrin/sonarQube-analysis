import pandas as pd
from scipy.stats import skew
import pytest
def task_func(df):
    """
    Calculate the skewness of the last column of the dataframe.

    Args:
        df (pandas.DataFrame): The input dataframe.

    Returns:
        float: The skewness of the last column of the dataframe.

    Raises:
        ValueError: If the input is not a DataFrame or has no columns.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas.DataFrame")
    if len(df.columns) == 0:
        raise ValueError("DataFrame has no columns")
    return skew(df.iloc[:, -1])