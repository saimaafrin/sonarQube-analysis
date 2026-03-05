
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def task_func(df, target_column, target_values=None):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("df must be a pandas DataFrame")
    if not isinstance(target_column, str):
        raise ValueError("target_column must be a string")
    if not isinstance(target_values, (np.ndarray, list)):
        raise ValueError("target_values must be an array-like object")

    # Replace elements not in target_values with zero
    for col in df.columns:
        df[col] = df[col].astype(str).str.replace(r'[^0-9]'.join(target_values.astype(str)), '0', regex=True).astype(float)

    # Initialize and fit the linear regression model
    model = LinearRegression()
    model.fit(df, df[target_column])

    return model