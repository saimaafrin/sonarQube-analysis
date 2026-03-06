import pandas as pd
import numpy as np
import statsmodels.api as sm
def task_func(
    array: list, random_seed: int = 0
) -> (pd.DataFrame, sm.regression.linear_model.RegressionResultsWrapper):
    """
    Generate a Pandas DataFrame from a 2D list and perform a multiple linear regression.

    The function first validates the input list, creates a DataFrame, separates independent and dependent variables,
    adds a constant to the model, and fits a linear regression using statsmodels.

    Parameters:
    - array (list of list of int): A 2D list where each sub-list represents a row of data.
                                   Each sub-list should have exactly 5 elements, where the first 4 elements are
                                   treated as independent variables ('A', 'B', 'C', 'D') and the last element is
                                   the dependent (Response) variable.

    - random_seed (int): A seed for reproducibility in numpy for statsmodels. Defaults to 0.

    Returns:
    - df (pd.DataFrame): DataFrame with columns 'A', 'B', 'C', 'D', 'Response'.
    - results (statsmodels.RegressionResults): Results of the linear regression.

    Requirements:
    - pandas
    - numpy
    - statsmodels.api.sm

    Example:
    >>> df, results = task_func([[1,2,3,4,5], [6,7,8,9,10]])
    >>> print(df)
       A  B  C  D  Response
    0  1  2  3  4         5
    1  6  7  8  9        10
    """
    # Validate input
    if not isinstance(array, list):
        raise TypeError("Input must be a list.")
    if not isinstance(random_seed, int):
        raise TypeError("random_seed must be an integer.")
    if not all(isinstance(x, list) for x in array):
        raise TypeError("Input must be a list of lists.")
    if not all(len(x) == 5 for x in array):
        raise ValueError("Input must be a list of lists with 5 elements.")

    # Create DataFrame
    df = pd.DataFrame(array, columns=["A", "B", "C", "D", "Response"])

    # Separate independent and dependent variables
    X = df[["A", "B", "C", "D"]]
    y = df["Response"]

    # Add constant to the model
    X = sm.add_constant(X)

    # Fit linear regression
    results = sm.OLS(y, X).fit()

    return df, results