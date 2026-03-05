import numpy as np
from scipy.stats import mode
from scipy.stats import entropy
def task_func(numbers):
    """
    Calculates the mode and entropy of a numpy array constructed from a given list.
    
    Parameters:
    numbers (list): A list of numbers to calculate the mode and entropy for.
    
    Returns:
    dict: A dictionary containing the 'mode' and 'entropy' of the array with their respective calculated values.
    
    Raises:
    ValueError: If the input list `numbers` is empty.
    """
    if not numbers:
        raise ValueError("Input list 'numbers' cannot be empty.")
    
    # Convert the list to a numpy array
    array = np.array(numbers)
    
    # Calculate the mode
    mode_result = mode(array)
    mode_value = mode_result.mode[0]
    
    # Calculate the entropy (base 2)
    # First, calculate the frequency of each unique element
    unique_elements, counts = np.unique(array, return_counts=True)
    # Then, calculate the probability of each element
    probabilities = counts / len(array)
    # Finally, calculate the entropy
    entropy_value = entropy(probabilities, base=2)
    
    # Create the result dictionary
    result = {
        'mode': mode_value,
        'entropy': entropy_value
    }
    
    return result