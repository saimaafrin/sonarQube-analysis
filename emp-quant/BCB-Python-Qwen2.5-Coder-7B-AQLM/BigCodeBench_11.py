
import numpy as np
import itertools
import random

def task_func(T1, max_value=100):
    # Convert elements in 'T1' to integers
    int_list = list(itertools.chain.from_iterable(T1))
    int_list = [int(x) for x in int_list]
    
    # Calculate the total number of elements in the list
    total_elements = sum(int_list)
    
    # Create a list of random integers with the size equal to the sum of the integers
    random_list = [random.randint(0, max_value) for _ in range(total_elements)]
    
    # Calculate the 25th, 50th, and 75th percentiles
    p25 = np.percentile(random_list, 25)
    p50 = np.percentile(random_list, 50)
    p75 = np.percentile(random_list, 75)
    
    # Return the percentiles as a tuple
    return (p25, p50, p75)