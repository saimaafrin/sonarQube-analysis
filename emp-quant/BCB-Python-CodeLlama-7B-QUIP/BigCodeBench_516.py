
import pandas as pd
import numpy as np
import statsmodels.api as sm

def task_func(array, random_seed=0):
    # Validate input
    if not isinstance(array, list):
        raise ValueError("array must be a list")
    if len(array) < 2:
        raise ValueError("array must have at least 2 elements")
    if not all(isinstance(x, list) for x in array):
        raise ValueError("array must be a list of lists")
    if not all(len(x) == len(array[0]) for x in array):
        raise ValueError("array must be a list of lists with the same length")

    # Create DataFrame
    df = pd.DataFrame(array)

    # Separate independent and dependent variables
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    # Add constant to the model
    X = sm.add_constant(X, has_constant=True)

    # Fit linear regression
    results = sm.OLS(y, X).fit()

    return df, results