
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Constants
ARRAY_LENGTH = 10

def task_func():
    # Generate a random array
    random_array = np.random.rand(ARRAY_LENGTH)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Reshape the array to fit the scaler's expected input shape
    reshaped_array = random_array.reshape(-1, 1)
    
    # Apply min-max normalization
    scaled_array = scaler.fit_transform(reshaped_array)
    
    # Return the scaled array
    return scaled_array.flatten()