
import numpy as np
import random

def task_func(my_list):
    # Append a random integer between 0 and 100 to the list
    my_list.append(random.randint(0, 100))
    
    # Calculate the sum of the numbers in the modified list
    total_sum = sum(my_list)
    
    # Generate a numpy array of random floating-point numbers with the size of the total sum
    random_array = np.random.rand(total_sum)
    
    return random_array