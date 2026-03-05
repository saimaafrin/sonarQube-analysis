import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
def task_func(data, target_column, test_size=0.2, random_state=0) -> float:
    """
    Train a linear regression model on the provided data and return the model score of the test set.

    Args:
        data (pd.DataFrame): The data to be used for training.
        target_column (str): The name of the target column in the data.
        test_size (float, optional): The proportion of the data to be used for testing. Defaults to 0.2.
        random_state (int, optional): The random state to be used for splitting the data. Defaults to 0.

    Returns:
        float: The model's score.

    Raises:
        ValueError: If data is not a DataFrame.
        ValueError: If data is empty.
        ValueError: If target_column is not a column of data.
        ValueError: If data contains values that are not numeric.
        ValueError: If random_state is not an integer.
        ValueError: If test_size is not between 0 and 1.
    """
    # Check if data is a DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("data must be a DataFrame")

    # Check if data is empty
    if data.empty:
        raise ValueError("data must not be empty")

    # Check if target_column is a column of data
    if target_column not in data.columns:
        raise ValueError(f"{target_column} is not a column of data")

    # Check if data contains numeric values
    if not data[target_column].apply(np.isreal).all():
        raise ValueError("data must contain numeric values")

    # Check if random_state is an integer
    if not isinstance(random_state, int):
        raise ValueError("random_state must be an integer")

    # Check if test_size is between 0 and 1
    if not (0 <= test_size <= 1):
        raise ValueError("test_size must be between 0 and 1")

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        data.drop(target_column, axis=1),
        data[target_column],
        test_size=test_size,
        random_state=random_state,
    )

    # Train linear regression model on training data
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Get model score on test data
    score = model.score(X_test, y_test)

    return score
data = pd.DataFrame({
    'x1': np.random.random(500),
    'x2': np.random.random(500),
    'y': data['x1'] * 2 + 1,
})