
import numpy as np
from sklearn.linear_model import LinearRegression

def task_func(df):
    # Initialize the linear regression model
    model = LinearRegression()

    # Fit the model to the data
    model.fit(df[['feature']], df['value'])

    # Get the coefficients and intercept
    coefficients = model.coef_
    intercept = model.intercept_

    # Return the results as a dictionary
    return {'coefficients': coefficients, 'intercept': intercept}