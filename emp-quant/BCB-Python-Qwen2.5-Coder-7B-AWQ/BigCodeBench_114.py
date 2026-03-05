import numpy as np
from sklearn.preprocessing import MinMaxScaler
def task_func(my_dict):
    """
    Modifies the input dictionary by adding a key 'normalized_array' with the normalized values of the numpy array found under the 'array' key.
    
    Parameters:
    my_dict (dict): A dictionary containing a key 'array' with a numpy array as its value.
    
    Returns:
    dict: The modified dictionary with an additional key 'normalized_array'.
    
    Raises:
    TypeError: If the value of the 'array' key is not a numpy array.
    """
    # Check if the 'array' key exists and its value is a numpy array
    if 'array' not in my_dict or not isinstance(my_dict['array'], np.ndarray):
        raise TypeError("The 'array' key must exist and its value must be a numpy array.")
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the array
    normalized_array = scaler.fit_transform(my_dict['array'])
    
    # Add the normalized array to the dictionary
    my_dict['normalized_array'] = normalized_array
    
    return my_dict
my_dict = {'array': np.array([[1, 2, 3], [4, 5, 6]])}