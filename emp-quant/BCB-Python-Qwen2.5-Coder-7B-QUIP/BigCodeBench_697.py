
import numpy as np
from sklearn.linear_model import LinearRegression

def task_func(df):
    # Ensure the dataframe has the necessary columns
    if 'feature' not in df.columns or 'value' not in df.columns:
        raise ValueError("DataFrame must contain 'feature' and 'value' columns.")
    
    # Convert the feature and value columns to numpy arrays
    X = df['feature'].values.reshape(-1, 1)
    y = df['value'].values
    
    # Initialize and fit the linear regression model
    model = LinearRegression()
    model.fit(X, y)
    
    # Get the coefficients and intercept
    coefficients = model.coef_
    intercept = model.intercept_
    
    # Return the result as a dictionary
    result = {
        'coefficients': coefficients,
        'intercept': intercept
    }
    
    return result