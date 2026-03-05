import numpy as np
from scipy.stats import mode
from scipy.stats import entropy
def task_func(numbers):
    if not numbers:
        raise ValueError("Input list 'numbers' is empty")
    
    # Convert the list to a numpy array
    array = np.array(numbers)
    
    # Calculate the mode of the array
    array_mode = mode(array)[0][0]
    
    # Calculate the entropy of the array (base 2)
    array_entropy = entropy(np.unique(array, return_counts=True)[1], base=2)
    
    # Create a dictionary with the mode and entropy
    result_dict = {'mode': array_mode, 'entropy': array_entropy}
    
    return result_dict