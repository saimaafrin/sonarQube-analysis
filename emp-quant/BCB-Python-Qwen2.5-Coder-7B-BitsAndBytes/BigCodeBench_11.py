
import numpy as np
import itertools
import random

def task_func(T1, max_value=100):
    # Convert string representations of integers in T1 to actual integers
    int_list = [int(num) for sublist in T1 for num in sublist]
    
    # Calculate the total number of random integers needed
    total_count = sum(int_list)
    
    # Generate a list of random integers
    random_numbers = [random.randint(0, max_value) for _ in range(total_count)]
    
    # Calculate the 25th, 50th, and 75th percentiles
    p25 = np.percentile(random_numbers, 25)
    p50 = np.percentile(random_numbers, 50)
    p75 = np.percentile(random_numbers, 75)
    
    # Return the result as a tuple
    return (p25, p50, p75)