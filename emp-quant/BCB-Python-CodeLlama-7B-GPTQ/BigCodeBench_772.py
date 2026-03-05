import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
def task_func(num_samples=1000, k=5, d=2, random_seed=None):
    """
    Generate a dataset consisting of random numbers sampled from a gaussian normal distribution that are transformed by applying a linear transformation.
    Standardize it with the StandardScaler of sklearn, and calculate the average square error between the original dataset and the standardized dataset.
    """
    # Generate random numbers sampled from a gaussian normal distribution
    data = np.random.normal(size=(num_samples, d))

    # Apply a linear transformation to the data
    transformed_data = data @ np.random.normal(size=(d, k))

    # Standardize the data using the StandardScaler of sklearn
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(transformed_data)

    # Calculate the average square error between the original and standardized data
    mse = mean_squared_error(data, standardized_data)

    return mse