import numpy as np
from sklearn.preprocessing import MinMaxScaler
ARRAY_LENGTH = 10
def task_func():
    # Generate a random array
    random_array = np.random.rand(ARRAY_LENGTH)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Reshape the array to fit the scaler
    reshaped_array = random_array.reshape(-1, 1)
    
    # Apply min-max normalization
    scaled_array = scaler.fit_transform(reshaped_array)
    
    # Reshape back to the original shape
    scaled_array = scaled_array.reshape(ARRAY_LENGTH)
    
    return scaled_array