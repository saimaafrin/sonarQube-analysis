
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def task_func(df: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the MinMax-normalized cumulative sum for each numeric column in the given DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: A DataFrame where each column contains the normalized cumulative sum of the
        respective column in the input DataFrame, retaining the original column names.

    Raises:
        TypeError: If the DataFrame contains non-numeric data types.
        ValueError: If the DataFrame is empty or contains NaN values.
    """
    # Check if the DataFrame contains non-numeric data types
    if not all(df.dtypes == np.number):
        raise TypeError("DataFrame contains non-numeric data types")

    # Check if the DataFrame is empty or contains NaN values
    if df.isnull().values.any() or df.empty:
        raise ValueError("DataFrame is empty or contains NaN values")

    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()

    # Compute the normalized cumulative sum for each numeric column
    normalized_cumsum = df.apply(lambda x: scaler.fit_transform(x.cumsum()))

    # Return the normalized cumulative sum as a DataFrame
    return normalized_cumsum