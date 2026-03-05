import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
def task_func(df, target_column, target_values=None):
    """
    Replace all elements in DataFrame columns that are not present in the target_values array with zeros, and then perform a linear regression using the target column.

    Parameters:
    df (pandas.DataFrame): The input DataFrame.
    target_column (str): The name of the target column.
    target_values (array-like, optional): The target values to be used for the regression.

    Returns:
    LinearRegression: The trained Linear Regression model.

    Raises:
    ValueError: If df is not a DataFrame or if target_column is not a string or if target_values is not an array-like object.
    """
    # Check if df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("df must be a pandas.DataFrame")

    # Check if target_column is a string
    if not isinstance(target_column, str):
        raise ValueError("target_column must be a string")

    # Check if target_values is an array-like object
    if not isinstance(target_values, (list, np.ndarray)):
        raise ValueError("target_values must be an array-like object")

    # Replace all elements in DataFrame columns that are not present in the target_values array with zeros
    df = df.replace(to_replace=df.columns.difference(target_values), value=0)

    # Perform linear regression using the target column
    model = LinearRegression().fit(df[target_column], df[target_values])

    return model
rng = np.random.default_rng(seed=0)
df = pd.DataFrame(rng.integers(0, 100, size=(1000, 5)), columns=['A', 'B', 'C', 'D', 'predict'])