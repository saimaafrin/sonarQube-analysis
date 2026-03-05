
import numpy as np
import random

def task_func(my_list):
    # Append a random integer between 0 and 100 to the list
    my_list.append(random.randint(0, 100))
    
    # Calculate the sum of the modified list
    total = sum(my_list)
    
    # Generate a numpy array of random floating-point numbers
    random_array = np.random.rand(total)
    
    return random_array