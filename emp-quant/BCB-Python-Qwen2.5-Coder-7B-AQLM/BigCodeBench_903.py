
import pandas as pd
from sklearn.linear_model import LinearRegression

def task_func(d, target='z'):
    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(d)
    
    # Separate the features (x, y) and the target (z)
    X = df[['x', 'y']]
    y = df[target]
    
    # Create a LinearRegression model
    model = LinearRegression()
    
    # Fit the model to the data
    model.fit(X, y)
    
    # Return the model
    return model