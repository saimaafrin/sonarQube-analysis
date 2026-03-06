
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def task_func(df, features):
    """
    Standardizes the specified features in a DataFrame using standard scaling.

    Parameters:
    df (pandas.DataFrame): The input DataFrame containing the data.
    features (list of str): A list of column names to be standardized.

    Returns:
    pandas.DataFrame: The DataFrame with the standardized features.
    """
    scaler = StandardScaler()
    df[features] = scaler.fit_transform(df[features])
    return df