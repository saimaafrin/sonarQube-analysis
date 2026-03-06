
import pandas as pd
from sklearn.linear_model import LinearRegression

ROWS = 100
COLUMNS = ['X', 'Y']

def task_func(df):
    # Ensure the DataFrame has the correct columns
    if not all(col in df.columns for col in COLUMNS):
        raise ValueError("DataFrame must contain columns 'X' and 'Y'")
    
    # Split the DataFrame into features (X) and target (Y)
    X = df[COLUMNS[0]].values.reshape(-1, 1)
    y = df[COLUMNS[1]].values
    
    # Create a linear regression model
    model = LinearRegression()
    
    # Fit the model to the data
    model.fit(X, y)
    
    return model