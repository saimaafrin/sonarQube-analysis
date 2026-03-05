
import numpy as np
import itertools
import random

def task_func(T1, max_value=100):
    # Convert the tuple of tuples to a list of integers
    list_of_ints = [int(x) for x in T1]
    # Create a list of random integers
    random_list = [random.randint(0, max_value) for i in range(sum(list_of_ints))]
    # Calculate the 25th, 50th, and 75th percentiles of the list
    p25 = np.percentile(random_list, 25)
    p50 = np.percentile(random_list, 50)
    p75 = np.percentile(random_list, 75)
    # Return the tuple of percentiles
    return (p25, p50, p75)