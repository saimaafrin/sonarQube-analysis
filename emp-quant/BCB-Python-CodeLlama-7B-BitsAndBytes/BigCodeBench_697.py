
import numpy as np
from sklearn.linear_model import LinearRegression

def task_func(df):
    # Create a linear regression model
    model = LinearRegression()

    # Fit the model to the data
    model.fit(df[['feature']], df['value'])

    # Get the coefficients and intercept of the model
    coefficients = model.coef_
    intercept = model.intercept_

    # Create a dictionary with the results
    result = {'coefficients': coefficients, 'intercept': intercept}

    return result