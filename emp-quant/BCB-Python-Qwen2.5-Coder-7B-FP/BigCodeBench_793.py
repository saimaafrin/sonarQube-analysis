import numpy as np
import random
ELEMENTS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
def task_func(l=None):
    """
    This function takes a list 'l' and converts it into a numpy array.
    It then moves the first three elements of the array to the end.
    
    Parameters:
    l (list): The input list to be converted and processed.
    
    Returns:
    arr (numpy.ndarray): The processed array with the first three elements moved to the end.
    """
    if l is None:
        l = [random.choice(ELEMENTS) for _ in range(10)]
    
    # Convert list to numpy array
    arr = np.array(l)
    
    # Check if the array has at least 3 elements
    if len(arr) < 3:
        raise ValueError("Array must contain at least 3 elements")
    
    # Move the first three elements to the end
    arr = np.roll(arr, -3)
    
    return arr