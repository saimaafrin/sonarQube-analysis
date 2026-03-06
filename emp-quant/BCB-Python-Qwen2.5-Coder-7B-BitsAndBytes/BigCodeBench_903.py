
import pandas as pd
from sklearn.linear_model import LinearRegression

def task_func(d, target='z'):
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(d)
    
    # Extract the features (x and y) and the target variable (z)
    X = df[['x', 'y']]
    y = df[target]
    
    # Create a LinearRegression model
    model = LinearRegression()
    
    # Fit the model to the data
    model.fit(X, y)
    
    return model