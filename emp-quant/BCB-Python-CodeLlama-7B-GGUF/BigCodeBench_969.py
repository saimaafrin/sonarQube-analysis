
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def task_func(df: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the MinMax-normalized cumulative sum for each numeric column in the given DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame

    Returns:
        pd.DataFrame: A DataFrame where each column contains the normalized cumulative sum of the
            respective column in the input DataFrame, retaining the original column names.

    Raises:
        TypeError: If the DataFrame contains non-numeric data types.
        ValueError: If the DataFrame is empty or contains NaN values.
    """
    # Check if the DataFrame contains non-numeric data types
    if not all(isinstance(x, (np.number, np.bool_)) for x in df.dtypes):
        raise TypeError("DataFrame contains non-numeric data types")

    # Check if the DataFrame is empty or contains NaN values
    if df.empty or df.isnull().values.any():
        raise ValueError("DataFrame is empty or contains NaN values")

    # Compute the MinMax-normalized cumulative sum for each numeric column
    scaler = MinMaxScaler()
    df_scaled = scaler.fit_transform(df)

    # Compute the cumulative sum for each column
    df_cumsum = df_scaled.cumsum()

    # Normalize the cumulative sum by dividing by the maximum value in each column
    df_normalized = df_cumsum / df_cumsum.max(axis=0)

    # Return the normalized cumulative sum as a DataFrame
    return pd.DataFrame(df_normalized, columns=df.columns)