import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
def task_func(data, target_column, test_size=0.2, random_state=0) -> float:
    """
    Train a linear regression model and return the model score of the test set.

    Args:
        data (pd.DataFrame): The data to train the model on.
        target_column (str): The name of the target column in the data.
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
    # Check input data
    if not isinstance(data, pd.DataFrame):
        raise ValueError("data must be a DataFrame")
    if data.empty:
        raise ValueError("data must not be empty")
    if target_column not in data.columns:
        raise ValueError(f"target_column '{target_column}' is not a column of data")
    if not np.issubdtype(data[target_column].dtype, np.number):
        raise ValueError(f"data must contain numeric values for target_column '{target_column}'")
    if not isinstance(random_state, int):
        raise ValueError("random_state must be an integer")
    if not 0 <= test_size <= 1:
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
    y_pred = model.predict(X_test)
    score = model.score(X_test, y_test)

    return score
data = pd.DataFrame({
    'x1': np.random.random(500),
    'x2': np.random.random(500),
    'y': data['x1'] * 2 + 1,
})