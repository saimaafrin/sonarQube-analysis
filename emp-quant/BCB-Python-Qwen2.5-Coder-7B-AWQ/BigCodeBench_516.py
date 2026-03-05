import pandas as pd
import numpy as np
import statsmodels.api as sm
def task_func(
    array: list, random_seed: int = 0
) -> (pd.DataFrame, sm.regression.linear_model.RegressionResultsWrapper):
    # Validate the input list
    if not all(isinstance(sublist, list) for sublist in array):
        raise ValueError("Input must be a 2D list.")
    if not all(len(sublist) == len(array[0]) for sublist in array):
        raise ValueError("All sublists must have the same length.")
    
    # Create a DataFrame
    df = pd.DataFrame(array, columns=[f'Feature_{i+1}' for i in range(len(array[0]))])
    
    # Separate independent and dependent variables
    X = df.drop('Feature_4', axis=1)  # Assuming 'Response' is the last column
    y = df['Feature_4']
    
    # Add a constant to the model
    X = sm.add_constant(X)
    
    # Fit a linear regression using statsmodels
    results = sm.OLS(y, X).fit()
    
    return df, results