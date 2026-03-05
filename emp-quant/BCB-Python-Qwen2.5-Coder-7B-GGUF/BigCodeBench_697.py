
import numpy as np
from sklearn.linear_model import LinearRegression

def task_func(df):
    # Extract the feature and value columns from the dataframe
    X = df['feature'].values.reshape(-1, 1)
    y = df['value'].values
    
    # Create a linear regression model
    model = LinearRegression()
    
    # Fit the model to the data
    model.fit(X, y)
    
    # Get the coefficients and intercept of the model
    coefficients = model.coef_[0]
    intercept = model.intercept_
    
    # Create a dictionary to store the results
    result = {
        'coefficients': coefficients,
        'intercept': intercept
    }
    
    return result