
import pandas as pd
import numpy as np
import statsmodels.api as sm

def task_func(
    array: list, random_seed: int = 0
) -> (pd.DataFrame, sm.regression.linear_model.RegressionResultsWrapper):
    # Validate input
    if not isinstance(array, list) or not all(isinstance(sublist, list) for sublist in array):
        raise ValueError("Input must be a 2D list.")
    if len(array) < 2 or any(len(sublist) != len(array[0]) for sublist in array):
        raise ValueError("Input must be a rectangular 2D list.")
    
    # Create DataFrame
    df = pd.DataFrame(array, columns=[f'Var{i+1}' for i in range(len(array[0]))])
    
    # Separate independent and dependent variables
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    
    # Add a constant to the model
    X = sm.add_constant(X)
    
    # Fit linear regression
    np.random.seed(random_seed)
    results = sm.OLS(y, X).fit()
    
    return df, results