import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
def task_func(n_samples=100, n_features=10, random_seed=None):
    """
    Generates synthetic data, fits a linear regression model, and returns predictions, coefficients, intercept, and MSE.
    
    Parameters:
    n_samples (int): Number of samples in the dataset.
    n_features (int): Number of features in the dataset.
    random_seed (int): Seed for random number generation for reproducibility.
    
    Returns:
    tuple: A tuple containing:
        predictions (numpy.ndarray): The predicted values of the test set.
        coefficients (numpy.ndarray): Coefficients of the linear regression model.
        intercept (float): Intercept of the linear regression model.
        mse (float): Mean squared error of the model predictions.
    """
    # Set the random seed for reproducibility
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate synthetic data
    X, y = datasets.make_regression(n_samples=n_samples, n_features=n_features, noise=0.1, random_state=random_seed)
    
    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_seed)
    
    # Initialize and fit the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Make predictions on the test set
    predictions = model.predict(X_test)
    
    # Get the coefficients and intercept of the model
    coefficients = model.coef_
    intercept = model.intercept_
    
    # Calculate the mean squared error of the model predictions
    mse = mean_squared_error(y_test, predictions)
    
    return predictions, coefficients, intercept, mse