import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
def task_func(n_samples=100, n_features=10, random_seed=None):
    """
    Generate synthetic data using a simple regression model, fit a linear regression model to the data,
    and return the predicted values along with the coefficients and intercept of the model.

    Parameters:
    - n_samples (int): The number of samples for the synthetic data. Default is 100.
    - n_features (int): The number of features for the synthetic data. Default is 10.
    - random_seed (int, optional): The seed for reproducibility. Default is None.

    Returns:
    - tuple: A tuple containing:
        - predictions (numpy.ndarray): The predicted values of the test set.
        - coefficients (numpy.ndarray): Coefficients of the linear regression model.
        - intercept (float): Intercept of the linear regression model.
        - mse (float): Mean squared error of the model predictions.

    Requirements:
    - numpy
    - sklearn.datasets.make_regression
    - sklearn.model_selection.train_test_split
    - sklearn.linear_model.LinearRegression
    
    Example:
    >>> predictions, coefficients, intercept, mse = task_func(100, 5, random_seed=42)
    >>> predictions[:3]
    array([ 180.79207843, -295.0210232 ,  118.23799221])
    >>> round(mse, 4)
    0.0113
    """
    # Generate synthetic data
    X, y = datasets.make_regression(n_samples=n_samples, n_features=n_features, random_state=random_seed)

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_seed)

    # Fit a linear regression model to the training set
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict the values for the test set
    predictions = model.predict(X_test)

    # Return the predicted values, coefficients, intercept, and mean squared error
    return predictions, model.coef_, model.intercept_, np.mean((predictions - y_test) ** 2)