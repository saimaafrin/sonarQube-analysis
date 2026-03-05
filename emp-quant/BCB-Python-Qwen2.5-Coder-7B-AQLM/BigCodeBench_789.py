
import numpy as np
from sklearn.preprocessing import MinMaxScaler
# Constants
ARRAY_LENGTH = 10

def task_func():
    # Generate a random array
    random_array = np.random.rand(ARRAY_LENGTH)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Reshape the array to fit the scaler
    random_array_reshaped = random_array.reshape(-1, 1)
    
    # Apply min-max normalization
    scaled_array_reshaped = scaler.fit_transform(random_array_reshaped)
    
    # Reshape back to the original shape
    scaled_array = scaled_array_reshaped.reshape(ARRAY_LENGTH)
    
    return scaled_array