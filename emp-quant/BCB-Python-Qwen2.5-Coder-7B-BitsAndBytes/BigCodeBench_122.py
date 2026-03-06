
import numpy as np
import random

def task_func(my_list):
    # Append a random integer between 0 and 100 to my_list
    my_list.append(random.randint(0, 100))
    
    # Calculate the sum of the modified list
    total_sum = sum(my_list)
    
    # Generate an array of random floating-point numbers with the calculated size
    result_array = np.random.rand(total_sum)
    
    return result_array