
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

def task_func(num_samples=1000, k=5, d=2, random_seed=None):
    # Generate random numbers sampled from a gaussian normal distribution
    X = np.random.normal(size=(num_samples, k))

    # Apply a linear transformation to the data
    X_transformed = X @ np.random.normal(size=(k, d))

    # Standardize the data using StandardScaler
    scaler = StandardScaler()
    X_standardized = scaler.fit_transform(X_transformed)

    # Calculate the mean squared error between the original and standardized data
    mse = mean_squared_error(X, X_standardized)

    return mse