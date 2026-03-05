import pandas as pd
import numpy as np
import statsmodels.api as sm
def task_func(array: list, random_seed: int = 0) -> (pd.DataFrame, sm.regression.linear_model.RegressionResultsWrapper):
    """
    Generate a Pandas DataFrame from a 2D list and perform a multiple linear regression.

    Parameters
    ----------
    array : list
        A 2D list of data.
    random_seed : int, optional
        A seed for reproducibility in numpy for statsmodels. Defaults to 0.

    Returns
    -------
    df : pd.DataFrame
        DataFrame with columns 'A', 'B', 'C', 'D', 'Response'.
    results : sm.regression.linear_model.RegressionResultsWrapper
        Results of the linear regression.
    """
    # Validate input
    if not isinstance(array, list):
        raise ValueError("Input must be a list.")
    if not all(isinstance(row, list) for row in array):
        raise ValueError("Input must be a list of lists.")
    if not all(len(row) == 5 for row in array):
        raise ValueError("Input must be a list of lists with 5 elements.")

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