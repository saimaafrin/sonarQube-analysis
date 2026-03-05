
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def task_func(n_samples=100, n_features=10, random_seed=None):
    # Generate synthetic data
    X = np.random.rand(n_samples, n_features)
    y = np.random.rand(n_samples)

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_seed)

    # Fit linear regression model to training data
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions on test data
    predictions = model.predict(X_test)

    # Calculate mean squared error
    mse = np.mean((y_test - predictions) ** 2)

    # Return results
    return (predictions, model.coef_, model.intercept_, mse)