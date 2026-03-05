
import pandas as pd
import numpy as np
import statsmodels.api as sm

def task_func(array: list, random_seed: int = 0) -> (pd.DataFrame, sm.regression.linear_model.RegressionResultsWrapper):
    # Validate input list
    if not isinstance(array, list) or len(array) < 2:
        raise ValueError("Input list must be a list of at least two elements.")

    # Create DataFrame
    df = pd.DataFrame(array)

    # Separate independent and dependent variables
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    # Add constant to model
    X = sm.add_constant(X)

    # Fit linear regression
    results = sm.OLS(y, X).fit()

    return df, results