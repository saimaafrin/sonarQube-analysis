import pandas as pd
from sklearn.linear_model import LinearRegression
def task_func(d, target='z'):
    """
    Perform linear regression on the given data.

    Parameters:
    - d: List of dictionaries, where each dictionary represents a data point with keys 'x', 'y', and 'z'.
    - target: The target variable to predict ('x', 'y', or 'z'). Default is 'z'.

    Returns:
    - A LinearRegression model trained on the data.
    """
    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(d)
    
    # Select the features and target variable
    X = df[['x', 'y']]
    y = df[target]
    
    # Create and train the LinearRegression model
    model = LinearRegression()
    model.fit(X, y)
    
    return model
data = [{'x': 4, 'y': 20, 'z': 10}, {'x': 5, 'y': 25, 'z': 15}, {'x': 6, 'y': 5, 'z': 20}]