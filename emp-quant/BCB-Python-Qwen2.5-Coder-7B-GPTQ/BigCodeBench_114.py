import numpy as np
from sklearn.preprocessing import MinMaxScaler
def task_func(my_dict):
    """
    Updates a dictionary by adding a normalized version of a numpy array found under the 'array' key.
    The normalization is performed using MinMaxScaler, scaling each value to fall between 0 and 1.
    
    Args:
    my_dict (dict): A dictionary with a key 'array' whose value is a numpy array.
    
    Returns:
    dict: The dictionary after adding a key 'normalized_array' with the normalized values.
    
    Raises:
    TypeError: If the value of the 'array' key in my_dict is not a numpy array.
    """
    # Check if 'array' key exists and its value is a numpy array
    if 'array' not in my_dict or not isinstance(my_dict['array'], np.ndarray):
        raise TypeError("The value of the 'array' key must be a numpy array.")
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the array
    normalized_array = scaler.fit_transform(my_dict['array'].reshape(-1, 1))
    
    # Add the normalized array to the dictionary
    my_dict['normalized_array'] = normalized_array
    
    return my_dict
my_dict = {'array': np.array([1, 2, 3, 4, 5])}