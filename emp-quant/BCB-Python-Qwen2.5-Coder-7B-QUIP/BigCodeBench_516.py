
import pandas as pd
import numpy as np
import statsmodels.api as sm

def task_func(
    array: list, random_seed: int = 0
) -> (pd.DataFrame, sm.regression.linear_model.RegressionResultsWrapper):
    # Validate input
    if not isinstance(array, list) or not all(isinstance(row, list) for row in array):
        raise ValueError("Input must be a 2D list")
    if not all(isinstance(item, (int, float)) for item in array):
        raise ValueError("All elements in the 2D list must be numbers")
    
    # Create DataFrame
    df = pd.DataFrame(array, columns=['A', 'B', 'C', 'D'])
    
    # Separate independent and dependent variables
    X = df[['A', 'B', 'C']]
    y = df['D']
    
    # Add a constant to the model
    X = sm.add_constant(X)
    
    # Fit a linear regression
    results = sm.OLS(y, X).fit(random_state=random_seed)
    
    return df, results