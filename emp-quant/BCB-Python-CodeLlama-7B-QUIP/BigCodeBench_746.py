
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def task_func(df, target_column, target_values=None):
    # Check if df is a DataFrame and target_column is a string
    if not (isinstance(df, pd.DataFrame) and isinstance(target_column, str)):
        raise ValueError("df must be a DataFrame and target_column must be a string")

    # Replace all non-target values with zeros
    for col in df.columns:
        if col != target_column:
            df[col] = 0

    # Perform linear regression
    model = LinearRegression().fit(df, df[target_column])

    # Return the trained model
    return model