
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def task_func(df, dct, columns=None):
    # Check if input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")

    # Create a copy of the DataFrame to avoid mutating the original
    df_copy = df.copy()

    # Encode categorical columns
    for col in dct:
        if df_copy[col].dtype == "object":
            le = LabelEncoder()
            df_copy[col] = le.fit_transform(df_copy[col])

    # Standardize numerical columns
    for col in dct:
        if df_copy[col].dtype == "float64":
            mean = df_copy[col].mean()
            std = df_copy[col].std()
            df_copy[col] = (df_copy[col] - mean) / std

    return df_copy