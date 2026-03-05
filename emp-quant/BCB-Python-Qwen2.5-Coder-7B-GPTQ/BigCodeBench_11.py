import numpy as np
import itertools
import random
def task_func(T1, max_value=100):
    # Convert elements in 'T1' to integers
    int_list = [int(item) for sublist in T1 for item in sublist]
    
    # Calculate the total number of random integers to generate
    total_count = sum(int_list)
    
    # Generate a list of random integers
    random_integers = [random.randint(0, max_value) for _ in range(total_count)]
    
    # Calculate the 25th, 50th, and 75th percentiles
    p25 = np.percentile(random_integers, 25)
    p50 = np.percentile(random_integers, 50)
    p75 = np.percentile(random_integers, 75)
    
    # Return the percentiles as a tuple
    return (p25, p50, p75)
T1 = ((1, 2, 3), (4, 5, 6))