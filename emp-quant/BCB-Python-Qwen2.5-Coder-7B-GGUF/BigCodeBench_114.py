
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def task_func(my_dict):
    if not isinstance(my_dict['array'], np.ndarray):
        raise TypeError("The value of the 'array' key must be a numpy array")
    
    scaler = MinMaxScaler()
    normalized_array = scaler.fit_transform(my_dict['array'].reshape(-1, 1)).flatten()
    my_dict['normalized_array'] = normalized_array
    
    return my_dict