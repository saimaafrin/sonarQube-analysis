import pandas as pd
import numpy as np
import statsmodels.api as sm
def task_func(
    array: list, random_seed: int = 0
) -> (pd.DataFrame, sm.regression.linear_model.RegressionResultsWrapper):
    # Validate the input list
    if not all(isinstance(sublist, list) for sublist in array):
        raise ValueError("Input must be a 2D list")
    if not all(isinstance(item, (int, float)) for sublist in array for item in sublist):
        raise ValueError("All elements in the 2D list must be numbers")
    
    # Create a DataFrame
    df = pd.DataFrame(array, columns=['A', 'B', 'C', 'D'])
    
    # Separate independent and dependent variables
    X = df[['A', 'B', 'C', 'D']]
    y = df['A']  # Assuming 'A' is the dependent variable for this example
    
    # Add a constant to the model
    X = sm.add_constant(X)
    
    # Set the random seed for reproducibility
    np.random.seed(random_seed)
    
    # Fit a linear regression
    results = sm.OLS(y, X).fit()
    
    return df, results