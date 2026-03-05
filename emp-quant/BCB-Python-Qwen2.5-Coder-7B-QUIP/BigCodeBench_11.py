
import numpy as np
import itertools
import random

def task_func(T1, max_value=100):
    # Convert elements in T1 to integers
    int_list = [int(item) for item in itertools.chain.from_iterable(T1)]
    
    # Create a list of random integers
    random_list = [random.randint(0, max_value) for _ in range(sum(int_list))]
    
    # Calculate the 25th, 50th, and 75th percentiles
    p25 = np.percentile(random_list, 25)
    p50 = np.percentile(random_list, 50)
    p75 = np.percentile(random_list, 75)
    
    # Return the result as a tuple
    return (p25, p50, p75)