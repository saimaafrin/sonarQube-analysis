
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

def task_func(data, target_column, test_size=0.2, random_state=0) -> float:
    # Check if data is a DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("data must be a DataFrame")
    
    # Check if data is empty
    if data.empty:
        raise ValueError("data cannot be empty")
    
    # Check if target_column is a column of data
    if target_column not in data.columns:
        raise ValueError(f"target_column '{target_column}' not found in data")
    
    # Check if data contains only numeric values
    if not data.dtypes[0].name.startswith('float') and not data.dtypes[0].name.startswith('int'):
        raise ValueError("data must contain only numeric values")
    
    # Check if random_state is an integer
    if not isinstance(random_state, int):
        raise ValueError("random_state must be an integer")
    
    # Check if test_size is between 0 and 1
    if not (0 < test_size < 1):
        raise ValueError("test_size must be between 0 and 1")
    
    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(data, data[target_column], test_size=test_size, random_state=random_state)
    
    # Train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Return the model score of the test set
    return model.score(X_test, y_test)