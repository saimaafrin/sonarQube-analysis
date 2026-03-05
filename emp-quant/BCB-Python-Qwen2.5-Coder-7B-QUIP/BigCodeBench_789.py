
import numpy as np
from sklearn.preprocessing import MinMaxScaler
# Constants
ARRAY_LENGTH = 10

def task_func():
    # Generate a random array
    random_array = np.random.rand(ARRAY_LENGTH)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the array
    scaled_array = scaler.fit_transform(random_array.reshape(-1, 1))
    
    # Return the scaled array
    return scaled_array