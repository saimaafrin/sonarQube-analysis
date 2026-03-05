import numpy as np
import itertools
import random
import statistics
def task_func(T1, RANGE=100):
    # Convert elements in 'T1' to integers
    try:
        int_T1 = [int(x) for x in T1]
    except ValueError:
        raise ValueError("All elements in T1 must be convertible to integers")
    
    # Calculate the sum of the integers in T1
    total_sum = sum(int_T1)
    
    # Create a list of random integers
    random_list = [random.randint(0, RANGE) for _ in range(total_sum)]
    
    # Calculate mean, median, and mode
    mean = np.mean(random_list)
    median = np.median(random_list)
    mode = statistics.mode(random_list)
    
    # Return the results as a tuple
    return (mean, median, mode)