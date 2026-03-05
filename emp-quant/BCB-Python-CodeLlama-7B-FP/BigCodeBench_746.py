import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
def task_func(df, target_column, target_values=None):
    """
    Replace all elements in DataFrame columns that are not present in the target_values array with zeros, and then perform a linear regression using the target column.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("df is not a DataFrame")
    if not isinstance(target_column, str):
        raise ValueError("target_column is not a string")
    if not isinstance(target_values, (list, np.ndarray)):
        raise ValueError("target_values is not an array-like object")

    # Replace all elements in DataFrame columns that are not present in the target_values array with zeros
    for column in df.columns:
        if column != target_column:
            df[column] = df[column].replace(target_values, 0)

    # Perform linear regression using the target column
    model = LinearRegression().fit(df[target_column], df[target_values])

    return model
rng = np.random.default_rng(seed=0)
df = pd.DataFrame(rng.integers(0, 100, size=(1000, 5)), columns=['A', 'B', 'C', 'D', 'predict'])