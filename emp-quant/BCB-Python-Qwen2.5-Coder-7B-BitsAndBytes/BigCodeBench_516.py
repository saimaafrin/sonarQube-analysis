
import pandas as pd
import numpy as np
import statsmodels.api as sm

def task_func(
    array: list, random_seed: int = 0
) -> (pd.DataFrame, sm.regression.linear_model.RegressionResultsWrapper):
    # Validate the input list
    if not all(isinstance(sublist, list) for sublist in array):
        raise ValueError("Input must be a 2D list.")
    
    # Create a DataFrame from the 2D list
    df = pd.DataFrame(array)
    
    # Check if there is at least one column for independent variables and one for the response variable
    if df.shape[1] < 2:
        raise ValueError("Array must contain at least two columns: one or more independent variables and one response variable.")
    
    # Separate independent and dependent variables
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    
    # Add a constant to the model
    X = sm.add_constant(X)
    
    # Set the random seed for reproducibility
    np.random.seed(random_seed)
    
    # Fit a linear regression model
    results = sm.OLS(y, X).fit()
    
    return df, results