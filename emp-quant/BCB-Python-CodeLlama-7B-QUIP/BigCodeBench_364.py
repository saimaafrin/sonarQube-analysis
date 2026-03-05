
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# Constants
FEATURES = ['feature '+str(i) for i in range(1, 11)]
TARGET = 'target'
def task_func(df):
    # Check if input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(df[FEATURES], df[TARGET], test_size=0.3)
    # Train linear regression model
    model = LinearRegression().fit(X_train, y_train)
    return model