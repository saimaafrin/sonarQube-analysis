import numpy as np
import itertools
import random
def task_func(T1, max_value=100):
    """
    Converts elements in 'T1', a tuple of tuples containing string representations of integers, to integers and creates a list of random integers. The size of the list equals the sum of these integers. Returns the 25th, 50th, and 75th percentiles of this list.
    """
    # Convert string representations of integers to integers
    T1 = [tuple(map(int, tup)) for tup in T1]

    # Calculate the sum of the integers in T1
    sum_T1 = sum(tup[0] for tup in T1)

    # Create a list of random integers
    random_list = [random.randint(1, max_value) for _ in range(sum_T1)]

    # Calculate the 25th, 50th, and 75th percentiles of the list
    p25 = np.percentile(random_list, 25)
    p50 = np.percentile(random_list, 50)
    p75 = np.percentile(random_list, 75)

    # Return the 25th, 50th, and 75th percentiles of the list
    return (p25, p50, p75)
T1 = (('1', '2'), ('3', '4'), ('5', '6'))
max_value = 100