
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def task_func(my_dict):
    """
    Updates a dictionary by adding a normalized version of a numpy array found under the 'array' key.
    The normalization is performed using MinMaxScaler, scaling each value to fall between 0 and 1.
    
    Parameters:
    my_dict (dict): The dictionary to be updated.
    
    Raises:
    TypeError: If the value of the 'array' key in my_dict is not a numpy array.
    
    Returns:
    None: The dictionary is modified in-place.
    """
    if 'array' not in my_dict:
        raise KeyError("The dictionary must contain the 'array' key.")
    
    if not isinstance(my_dict['array'], np.ndarray):
        raise TypeError("The value of the 'array' key must be a numpy array.")
    
    scaler = MinMaxScaler()
    my_dict['array'] = scaler.fit_transform(my_dict['array'].reshape(-1, 1))
    
    my_dict['normalized_array'] = scaler.transform(my_dict['array'].reshape(-1, 1))
    
    print("dict:", my_dict)