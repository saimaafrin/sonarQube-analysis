
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

def task_func(data, target_column, test_size=0.2, random_state=0) -> float:
    """
    Train a linear regression model on the provided data and return the model score of the test set.

    Parameters:
    data (pd.DataFrame): The data to train the model on.
    target_column (str): The name of the column containing the target variable.
    test_size (float, optional): The proportion of the data to use for testing. Defaults to 0.2.
    random_state (int, optional): The random state to use for splitting the data. Defaults to 0.

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
    if not isinstance(data, pd.DataFrame):
        raise ValueError("data must be a DataFrame")
    if data.empty:
        raise ValueError("data must not be empty")
    if target_column not in data.columns:
        raise ValueError("target_column must be a column of data")
    if not np.issubdtype(data[target_column].dtype, np.number):
        raise ValueError("data must contain numeric values")
    if not isinstance(random_state, int):
        raise ValueError("random_state must be an integer")
    if not 0 <= test_size <= 1:
        raise ValueError("test_size must be between 0 and 1")

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        data.drop(target_column, axis=1),  # Features
        data[target_column],  # Target
        test_size=test_size,
        random_state=random_state,
    )

    # Train the linear regression model on the training data
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate the model on the test data
    y_pred = model.predict(X_test)
    score = model.score(X_test, y_test)

    return score