
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def task_func(my_dict):
    # Check if 'array' key exists and its value is a numpy array
    if 'array' not in my_dict or not isinstance(my_dict['array'], np.ndarray):
        raise TypeError("The value of 'array' key in my_dict must be a numpy array")

    # Normalize the array using MinMaxScaler
    scaler = MinMaxScaler()
    normalized_array = scaler.fit_transform(my_dict['array'])

    # Add the normalized array to the dictionary
    my_dict['normalized_array'] = normalized_array

    return my_dict