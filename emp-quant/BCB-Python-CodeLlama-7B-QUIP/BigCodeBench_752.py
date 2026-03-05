
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

def task_func(data, target_column, test_size=0.2, random_state = 0) -> float:
    # Check if data is a DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("data must be a DataFrame")

    # Check if data is not empty
    if data.empty:
        raise ValueError("data is empty")

    # Check if target_column is a column of data
    if target_column not in data.columns:
        raise ValueError("target_column is not a column of data")

    # Check if data contains only numeric values
    if not data.select(target_column).select(lambda x: x.isnumeric).all():
        raise ValueError("data contains non-numeric values")

    # Check if random_state is an integer
    if not isinstance(random_state, int):
        raise ValueError("random_state must be an integer")

    # Check if test_size is between 0 and 1
    if not 0 <= test_size <= 1:
        raise ValueError("test_size must be between 0 and 1")

    # Split data into training and test sets
    train_data, test_data, train_targets, test_targets = train_test_split(data, data[target_column], test_size=test_size, random_state=random_state)

    # Train a linear regression model on the training data
    model = LinearRegression()
    model.fit(train_data, train_targets)

    # Evaluate the model on the test data
    test_preds = model.predict(test_data)
    test_mse = np.mean((test_preds - test_targets) ** 2)

    # Return the model's score
    return test_mse