import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
FEATURES = ['feature '+str(i) for i in range(1, 11)]
TARGET = 'target'
def task_func(df):
    """
    Train a linear regression model on a given DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        LinearRegression: The trained linear regression model.

    Raises:
        ValueError: If the input df is not a DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError('Input df must be a DataFrame')

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(df[FEATURES], df[TARGET], test_size=0.2, random_state=42)

    # Train a linear regression model on the training data
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate the model on the testing data
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean squared error: {mse:.2f}')

    return model
df = pd.DataFrame({
    'feature 1': [1, 2, 3, 4, 5],
    'feature 2': [2, 4, 6, 8, 10],
    'feature 3': [3, 6, 9, 12, 15],
    'feature 4': [4, 8, 12, 16, 20],
    'feature 5': [5, 10, 15, 20, 25],
    'feature 6': [6, 12, 18, 24, 30],
    'feature 7': [7, 14, 21, 28, 35],
    'feature 8': [8, 16, 24, 32, 40],
    'feature 9': [9, 18, 27, 36, 45],
    'feature 10': [10, 20, 30, 40, 50],
    'target': [10, 20, 30, 40, 50]
})