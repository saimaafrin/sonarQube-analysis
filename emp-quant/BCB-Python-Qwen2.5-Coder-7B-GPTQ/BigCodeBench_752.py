import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
def task_func(data, target_column, test_size=0.2, random_state=0) -> float:
    # Check if data is a DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Data must be a pandas DataFrame.")
    
    # Check if data is empty
    if data.empty:
        raise ValueError("Data cannot be empty.")
    
    # Check if target_column is a column of data
    if target_column not in data.columns:
        raise ValueError(f"Target column '{target_column}' is not a column of data.")
    
    # Check if data contains values that are not numeric
    if not np.issubdtype(data.dtypes[target_column], np.number):
        raise ValueError(f"Target column '{target_column}' must contain numeric values.")
    
    # Check if random_state is an integer
    if not isinstance(random_state, int):
        raise ValueError("Random state must be an integer.")
    
    # Check if test_size is between 0 and 1
    if not (0 < test_size < 1):
        raise ValueError("Test size must be between 0 and 1.")
    
    # Split data into training and test sets
    X = data.drop(target_column, axis=1)
    y = data[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    # Train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Return the model score of the test set
    return model.score(X_test, y_test)