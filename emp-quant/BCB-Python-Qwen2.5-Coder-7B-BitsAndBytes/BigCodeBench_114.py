
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def task_func(my_dict):
    # Check if the 'array' key exists and its value is a numpy array
    if 'array' not in my_dict or not isinstance(my_dict['array'], np.ndarray):
        raise TypeError("The value of the 'array' key must be a numpy array.")
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the array
    normalized_array = scaler.fit_transform(my_dict['array'].reshape(-1, 1))
    
    # Add the normalized array back to the dictionary
    my_dict['normalized_array'] = normalized_array
    
    return my_dict