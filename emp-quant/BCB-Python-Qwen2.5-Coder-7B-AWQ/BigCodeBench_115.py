import numpy as np
from scipy.stats import mode
from scipy.stats import entropy
def task_func(numbers):
    """
    Calculates the mode and entropy of a numpy array constructed from a given list.
    
    Parameters:
    numbers (list): A list of numbers.
    
    Returns:
    dict: A dictionary containing the 'mode' and 'entropy' of the array with their respective calculated values.
    
    Raises:
    ValueError: If the input list `numbers` is empty.
    """
    if not numbers:
        raise ValueError("Input list 'numbers' is empty")
    
    # Convert the list to a numpy array
    array = np.array(numbers)
    
    # Calculate the mode
    array_mode = mode(array).mode[0]
    
    # Calculate the entropy (base 2)
    array_entropy = entropy(np.unique(array, return_counts=True)[1], base=2)
    
    # Create a dictionary with the mode and entropy
    result = {
        'mode': array_mode,
        'entropy': array_entropy
    }
    
    return result
numbers = [1, 2, 2, 3, 3, 3]