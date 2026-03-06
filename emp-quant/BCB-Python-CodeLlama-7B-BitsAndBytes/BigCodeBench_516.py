
import pandas as pd
import numpy as np
import statsmodels.api as sm

def task_func(array, random_seed=0):
    # Validate input list
    if not isinstance(array, list):
        raise ValueError("Input must be a list")
    if len(array) == 0:
        raise ValueError("Input list is empty")

    # Create DataFrame
    df = pd.DataFrame(array)

    # Separate independent and dependent variables
    X = df.drop('Response', axis=1)
    y = df['Response']

    # Add constant to model
    X = sm.add_constant(X)

    # Fit linear regression
    results = sm.OLS(y, X).fit()

    return df, results

df, results = task_func(array)
print(df)
print(results.summary())