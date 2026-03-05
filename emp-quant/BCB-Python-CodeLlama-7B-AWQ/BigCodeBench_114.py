import numpy as np
from sklearn.preprocessing import MinMaxScaler
def task_func(my_dict):
    """
    Updates a dictionary by adding a normalized version of a numpy array found under the 'array' key.
    The normalization is performed using MinMaxScaler, scaling each value to fall between 0 and 1.
    """
    if 'array' not in my_dict:
        raise TypeError("'array' key not found in dictionary")
    if not isinstance(my_dict['array'], np.ndarray):
        raise TypeError("'array' key value is not a numpy array")

    scaler = MinMaxScaler()
    my_dict['normalized_array'] = scaler.fit_transform(my_dict['array'])

    return my_dict
my_dict = {'array': np.array([1, 2, 3, 4, 5])}