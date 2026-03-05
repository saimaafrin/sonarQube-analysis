import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
def task_func(num_samples=1000, k=5, d=2, random_seed=None):
    """
    Generate a dataset of random numbers sampled from a Gaussian normal distribution,
    apply a linear transformation, standardize it, and calculate the mean squared error
    between the original and standardized dataset.

    Parameters:
    - num_samples: int, the number of samples in the dataset.
    - k: float, the slope of the linear transformation.
    - d: float, the intercept of the linear transformation.
    - random_seed: int, the seed for the random number generator for reproducibility.

    Returns:
    - float: The mean squared error between the original and standardized data.
    """
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate random data from a Gaussian normal distribution
    original_data = np.random.randn(num_samples)
    
    # Apply linear transformation
    transformed_data = k * original_data + d
    
    # Standardize the transformed data
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(transformed_data.reshape(-1, 1)).flatten()
    
    # Calculate the mean squared error
    mse = mean_squared_error(original_data, standardized_data)
    
    return mse