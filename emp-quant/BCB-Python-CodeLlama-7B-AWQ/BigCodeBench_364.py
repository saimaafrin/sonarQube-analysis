import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
FEATURES = ['feature '+str(i) for i in range(1, 11)]
TARGET = 'target'
def task_func(df):
    """
    Train a linear regression model on a given DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df must be a DataFrame")
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(df[FEATURES], df[TARGET], test_size=0.2, random_state=42)
    # Train linear regression model
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    # Evaluate model on test set
    y_pred = lr.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean squared error: {mse}")
    return lr