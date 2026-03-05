import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
def task_func(n_samples=100, n_features=10, random_seed=None):
    # Generate synthetic data
    X, y = datasets.make_regression(n_samples=n_samples, n_features=n_features, random_state=random_seed)

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_seed)

    # Fit linear regression model to training data
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions on test data
    y_pred = model.predict(X_test)

    # Calculate mean squared error
    mse = np.mean((y_test - y_pred) ** 2)

    # Return predictions, coefficients, intercept, and MSE
    return (y_pred, model.coef_, model.intercept_, mse)
n_samples = 100
n_features = 10
random_seed = 42
model = LinearRegression()
y_pred = model.predict(X_test)
mse = np.mean((y_test - y_pred) ** 2)