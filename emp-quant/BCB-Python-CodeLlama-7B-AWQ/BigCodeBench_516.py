import pandas as pd
import numpy as np
import statsmodels.api as sm
def task_func(
    array: list, random_seed: int = 0
) -> (pd.DataFrame, sm.regression.linear_model.RegressionResultsWrapper):
    """
    Generate a Pandas DataFrame from a 2D list and perform a multiple linear regression.
    The function first validates the input list, creates a DataFrame, separates independent and dependent variables, adds a constant to the model, and fits a linear regression using statsmodels.
    """
    # Validate input
    if not isinstance(array, list):
        raise ValueError("Input must be a list")
    if not all(isinstance(i, list) for i in array):
        raise ValueError("Input must be a list of lists")
    if not all(len(i) == 5 for i in array):
        raise ValueError("Input must be a list of lists with 5 elements")

    # Create DataFrame
    df = pd.DataFrame(array, columns=["A", "B", "C", "D", "Response"])

    # Separate independent and dependent variables
    X = df[["A", "B", "C", "D"]]
    y = df["Response"]

    # Add constant to model
    X = sm.add_constant(X)

    # Fit linear regression
    results = sm.OLS(y, X).fit()

    return df, results
array = [
    [1, 2, 3, 4, 5],
    [2, 4, 6, 8, 10],
    [3, 6, 9, 12, 15],
]