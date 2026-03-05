import numpy as np
from sklearn.linear_model import LinearRegression
def task_func(df):
    # Create a linear regression model
    model = LinearRegression()

    # Fit the model to the data
    model.fit(df[['feature']], df['value'])

    # Get the coefficients and intercept
    coefs = model.coef_
    intercept = model.intercept_

    # Create a dictionary with the results
    result = {'coefs': coefs, 'intercept': intercept}

    # Return the results
    return result
df = pd.DataFrame({'feature': [1, 2, 3, 4, 5], 'value': [10, 20, 30, 40, 50]})