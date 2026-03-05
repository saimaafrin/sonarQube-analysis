
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

def task_func(num_samples=1000, k=5, d=2, random_seed=None):
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate random numbers from a Gaussian normal distribution
    original_data = np.random.randn(num_samples)
    
    # Apply a linear transformation
    transformed_data = k * original_data + d
    
    # Standardize the transformed data
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(transformed_data.reshape(-1, 1)).flatten()
    
    # Calculate the mean squared error between the original and standardized data
    mse = mean_squared_error(original_data, standardized_data)
    
    return mse

mse = task_func(k=1, d=0)
print(mse)  # Output should be close to 0.001113785307245742