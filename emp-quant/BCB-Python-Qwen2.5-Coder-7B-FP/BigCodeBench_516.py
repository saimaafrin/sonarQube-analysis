import pandas as pd
import numpy as np
import statsmodels.api as sm
def task_func(
    array: list, random_seed: int = 0
) -> (pd.DataFrame, sm.regression.linear_model.RegressionResultsWrapper):
    """
    Generate a Pandas DataFrame from a 2D list and perform a multiple linear regression.
    
    Parameters:
    - array (list): A 2D list where the last column is the dependent variable and the rest are independent variables.
    - random_seed (int): A seed for reproducibility in numpy for statsmodels. Defaults to 0.
    
    Returns:
    - df (pd.DataFrame): DataFrame with columns 'A', 'B', 'C', 'D', 'Response'.
    - results (statsmodels.RegressionResultsWrapper): Results of the linear regression.
    """
    # Validate input
    if not isinstance(array, list) or not all(isinstance(row, list) for row in array):
        raise ValueError("Input must be a 2D list.")
    if len(array) == 0 or len(array[0]) == 0:
        raise ValueError("Input list cannot be empty.")
    
    # Create DataFrame
    df = pd.DataFrame(array, columns=[f'Feature_{i+1}' for i in range(len(array[0])-1)] + ['Response'])
    
    # Separate independent and dependent variables
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    
    # Add a constant to the model
    X = sm.add_constant(X)
    
    # Set random seed for reproducibility
    np.random.seed(random_seed)
    
    # Fit a linear regression
    results = sm.OLS(y, X).fit()
    
    return df, results
array = [
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7],
    [4, 5, 6, 7, 8],
    [5, 6, 7, 8, 9]
]