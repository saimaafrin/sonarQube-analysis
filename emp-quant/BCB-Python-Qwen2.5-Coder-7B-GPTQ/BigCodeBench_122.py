import numpy as np
import random
def task_func(my_list):
    # Append a random integer between 0 and 100 to the list
    my_list.append(random.randint(0, 100))
    
    # Calculate the sum of the modified list
    array_size = sum(my_list)
    
    # Generate a numpy array of random floating-point numbers with the calculated size
    result_array = np.random.rand(array_size)
    
    return result_array