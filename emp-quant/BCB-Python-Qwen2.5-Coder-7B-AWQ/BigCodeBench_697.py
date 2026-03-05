import numpy as np
from sklearn.linear_model import LinearRegression
def task_func(df):
    """
    Fits a linear regression model to the dataframe and returns the coefficients and intercept.

    Parameters:
    df (pd.DataFrame): A pandas DataFrame with at least two columns: 'feature' and 'value'.

    Returns:
    result (dict): A dictionary containing the coefficients and intercept of the fitted model.
    """
    # Extracting the feature and value columns
    X = df[['feature']]
    y = df['value']
    
    # Creating and fitting the linear regression model
    model = LinearRegression()
    model.fit(X, y)
    
    # Extracting the coefficients and intercept
    coefficients = model.coef_[0]
    intercept = model.intercept_
    
    # Returning the results in a dictionary
    result = {
        'coefficients': coefficients,
        'intercept': intercept
    }
    
    return result