
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def task_func(my_dict):
    if 'array' not in my_dict:
        raise TypeError("'array' key not found in dictionary")
    if not isinstance(my_dict['array'], np.ndarray):
        raise TypeError("'array' key value is not a numpy array")

    scaler = MinMaxScaler()
    normalized_array = scaler.fit_transform(my_dict['array'])
    my_dict['normalized_array'] = normalized_array
    return my_dict