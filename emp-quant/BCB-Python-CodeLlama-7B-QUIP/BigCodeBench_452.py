
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def task_func(n_samples=100, n_features=10, random_seed=None):
    # Generate synthetic data
    X = np.random.rand(n_samples, n_features)
    y = np.random.rand(n_samples)

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=random_seed)

    # Fit linear regression model
    model = LinearRegression().fit(X_train, y_train)

    # Get predicted values
    predictions = model.predict(X_test)

    # Get coefficients and intercept
    coefficients = model.coef_
    intercept = model.intercept_

    # Get mean squared error
    mse = np.mean((y_test - predictions) ** 2)

    return (predictions, coefficients, intercept, mse)