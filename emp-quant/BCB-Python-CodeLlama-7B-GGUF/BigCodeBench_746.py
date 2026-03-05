
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def task_func(df, target_column, target_values=None):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("df must be a DataFrame")
    if not isinstance(target_column, str):
        raise ValueError("target_column must be a string")
    if target_values is not None and not isinstance(target_values, (list, np.ndarray)):
        raise ValueError("target_values must be an array-like object")

    # Replace all elements in DataFrame columns that are not present in the target_values array with zeros
    if target_values is not None:
        for col in df.columns:
            df[col] = df[col].replace(target_values, 0)

    # Perform linear regression using the target column
    X = df.drop(columns=target_column)
    y = df[target_column]
    model = LinearRegression().fit(X, y)

    return model