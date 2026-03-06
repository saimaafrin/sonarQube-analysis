
import numpy as np
from sklearn.linear_model import LinearRegression

def task_func(df):
    # Extract feature and target from the DataFrame
    X = df[['feature']].values
    y = df['value'].values
    
    # Create a linear regression model
    model = LinearRegression()
    
    # Fit the model
    model.fit(X, y)
    
    # Get the coefficients and intercept
    coefficients = model.coef_[0]
    intercept = model.intercept_
    
    # Return the results in a dictionary
    result = {
        'coefficients': coefficients,
        'intercept': intercept
    }
    
    return result