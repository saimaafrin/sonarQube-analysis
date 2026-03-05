import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
def task_func(n_samples=100, n_features=10, random_seed=None):
    # Generate synthetic data
    X, y = datasets.make_regression(n_samples=n_samples, n_features=n_features, random_state=random_seed)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_seed)

    # Fit linear regression model to training data
    reg = LinearRegression()
    reg.fit(X_train, y_train)

    # Make predictions on test data
    y_pred = reg.predict(X_test)

    # Calculate mean squared error
    mse = np.mean((y_test - y_pred) ** 2)

    # Return predictions, coefficients, intercept, and MSE
    return y_pred, reg.coef_, reg.intercept_, mse
n_samples = 100
n_features = 10
random_seed = 42
reg = LinearRegression()
y_pred = reg.predict(X_test)
mse = np.mean((y_test - y_pred) ** 2)