
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

def task_func(data, target_column, test_size=0.2, random_state=0) -> float:
    # Check if data is a DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("data is not a DataFrame")

    # Check if data is empty
    if data.empty:
        raise ValueError("data is empty")

    # Check if target_column is a column of data
    if target_column not in data.columns:
        raise ValueError("target_column is not a column of data")

    # Check if data contains numeric values
    if not data[target_column].dtype == np.float64:
        raise ValueError("data contains non-numeric values")

    # Check if random_state is an integer
    if not isinstance(random_state, int):
        raise ValueError("random_state is not an integer")

    # Check if test_size is between 0 and 1
    if not (0 <= test_size <= 1):
        raise ValueError("test_size is not between 0 and 1")

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(data.drop(target_column, axis=1), data[target_column], test_size=test_size, random_state=random_state)

    # Train linear regression model on training data
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Get model score on test data
    score = model.score(X_test, y_test)

    return score