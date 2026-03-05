
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def task_func(df: pd.DataFrame) -> pd.DataFrame:
    # Check if the DataFrame contains non-numeric data types
    if not all(df.dtypes == np.number):
        raise TypeError("The DataFrame contains non-numeric data types")

    # Check if the DataFrame is empty or contains NaN values
    if df.empty or df.isnull().any():
        raise ValueError("The DataFrame is empty or contains NaN values")

    # Normalize the DataFrame using MinMaxScaler
    scaler = MinMaxScaler()
    df_scaled = scaler.fit_transform(df)

    # Compute the cumulative sum for each column
    cumsum = df_scaled.cumsum()

    # Normalize the cumulative sum by the maximum value in each column
    cumsum_normalized = cumsum / cumsum.max()

    return cumsum_normalized