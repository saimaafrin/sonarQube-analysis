
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def task_func(n_samples=100, n_features=10, random_seed=None):
    # Set the random seed for reproducibility
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate synthetic data
    X, y = datasets.make_regression(n_samples=n_samples, n_features=n_features, noise=0.1, random_state=random_seed)
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_seed)
    
    # Fit a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Get the predicted values
    predictions = model.predict(X_test)
    
    # Get the coefficients and intercept
    coefficients = model.coef_
    intercept = model.intercept_
    
    # Calculate the mean squared error
    mse = np.mean((predictions - y_test) ** 2)
    
    return predictions, coefficients, intercept, mse