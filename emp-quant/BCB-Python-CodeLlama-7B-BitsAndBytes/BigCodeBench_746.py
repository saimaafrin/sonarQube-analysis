
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def task_func(df, target_column, target_values=None):
    # Check if df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("df must be a DataFrame")

    # Check if target_column is a string
    if not isinstance(target_column, str):
        raise ValueError("target_column must be a string")

    # Check if target_values is an array-like object
    if not isinstance(target_values, np.ndarray):
        raise ValueError("target_values must be an array-like object")

    # Replace all elements in DataFrame columns that are not present in the target_values array with zeros
    df = df.replace(to_replace=df.columns.difference(target_values), value=0)

    # Perform a linear regression using the target column
    model = LinearRegression().fit(df[target_column], df['predict'])

    # Print the coefficients and intercept of the trained Linear Regression model
    print(model.coef_)
    print(model.intercept_)

    return model

# Generate a random DataFrame with 1000 rows and 5 columns
rng = np.random.default_rng(seed=0)
df = pd.DataFrame(rng.integers(0, 100, size=(1000, 5)), columns=['A', 'B', 'C', 'D', 'predict'])

# Call the task_func function with the target column and target values
model = task_func(df, 'predict', target_values=['A', 'B', 'C'])

# Print the coefficients and intercept of the trained Linear Regression model
print(model.coef_)
print(model.intercept_)