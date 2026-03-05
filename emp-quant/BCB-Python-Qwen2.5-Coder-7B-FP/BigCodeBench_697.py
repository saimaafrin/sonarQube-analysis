import numpy as np
from sklearn.linear_model import LinearRegression
def task_func(df):
    """
    Fits a linear regression model to the dataframe and returns the coefficients and intercept.

    Parameters:
    df (pd.DataFrame): A pandas DataFrame with at least two columns: 'feature' and 'value'.

    Returns:
    result (dict): A dictionary with the coefficients and the intercept of the fitted linear regression model.
    """
    # Extract the feature and value columns from the dataframe
    X = df[['feature']]
    y = df['value']
    
    # Initialize and fit the linear regression model
    model = LinearRegression()
    model.fit(X, y)
    
    # Extract the coefficients and intercept
    coefficients = model.coef_[0]
    intercept = model.intercept_
    
    # Return the results in a dictionary
    result = {
        'coefficients': coefficients,
        'intercept': intercept
    }
    
    return result