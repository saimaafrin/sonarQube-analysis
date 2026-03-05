import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
def task_func(num_samples=1000, k=5, d=2, random_seed=None):
    """
    Generate a dataset consisting of random numbers sampled from a Gaussian normal distribution that are transformed by applying a linear transformation.
    Standardize it with the StandardScaler of sklearn, and calculate the average square error between the original dataset and the standardized dataset.
    """
    # Generate random numbers sampled from a Gaussian normal distribution
    data = np.random.normal(size=(num_samples, d))

    # Apply a linear transformation to the data
    data = data @ np.random.normal(size=(k, d))

    # Standardize the data with the StandardScaler of sklearn
    scaler = StandardScaler()
    data_standardized = scaler.fit_transform(data)

    # Calculate the average square error between the original dataset and the standardized dataset
    mse = mean_squared_error(data, data_standardized)

    return mse