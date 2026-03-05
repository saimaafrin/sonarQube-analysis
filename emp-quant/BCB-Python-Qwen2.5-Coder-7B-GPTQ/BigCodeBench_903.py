import pandas as pd
from sklearn.linear_model import LinearRegression
def task_func(d, target='z'):
    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(d)
    
    # Extract the target variable and the features
    X = df.drop(target, axis=1)
    y = df[target]
    
    # Create and fit the LinearRegression model
    model = LinearRegression()
    model.fit(X, y)
    
    return model
data = [{'x': 4, 'y': 20, 'z': 10}, {'x': 5, 'y': 25, 'z': 15}, {'x': 6, 'y': 5, 'z': 20}]