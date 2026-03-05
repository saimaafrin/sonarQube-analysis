
import numpy as np
from scipy.stats import mode
from scipy.stats import entropy

def task_func(numbers):
    if not numbers:
        raise ValueError("Input list 'numbers' is empty")
    
    # Convert the list to a numpy array
    array = np.array(numbers)
    
    # Calculate the mode
    mode_val = mode(array)[0]
    
    # Calculate the entropy (base 2)
    entropy_val = entropy(array, base=2)
    
    # Create and return the dictionary
    result_dict = {
        'mode': mode_val,
        'entropy': entropy_val
    }
    
    return result_dict