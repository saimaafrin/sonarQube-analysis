import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
def task_func(df, target_column, target_values=None):
    """
    Replace all elements in DataFrame columns that are not present in the target_values array with zeros,
    and then perform a linear regression using the target column.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    target_column (str): The name of the target column for regression.
    target_values (array-like, optional): The values to keep in the DataFrame columns. Defaults to None.

    Returns:
    LinearRegression: The trained Linear Regression model.

    Raises:
    ValueError: If df is not a DataFrame or if target_column is not a string or if target_values is not an array-like object
    """
    # Check if df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("df must be a DataFrame")
    
    # Check if target_column is a string
    if not isinstance(target_column, str):
        raise ValueError("target_column must be a string")
    
    # Check if target_values is an array-like object
    if target_values is not None and not hasattr(target_values, '__iter__'):
        raise ValueError("target_values must be an array-like object")
    
    # Replace elements not in target_values with zeros
    if target_values is not None:
        for col in df.columns:
            df[col] = df[col].apply(lambda x: x if x in target_values else 0)
    
    # Perform linear regression
    X = df.drop(target_column, axis=1)
    y = df[target_column]
    model = LinearRegression()
    model.fit(X, y)
    
    return model
rng = np.random.default_rng(seed=0)
df = pd.DataFrame(rng.integers(0, 100, size=(1000, 5)), columns=['A', 'B', 'C', 'D', 'predict'])