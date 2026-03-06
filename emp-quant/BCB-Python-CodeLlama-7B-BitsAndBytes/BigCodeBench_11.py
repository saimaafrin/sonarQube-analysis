
import numpy as np
import itertools
import random

def task_func(T1, max_value=100):
    # Convert elements in T1 to integers
    T1_ints = [int(x) for x in T1]

    # Create a list of random integers
    rand_ints = [random.randint(0, max_value) for _ in range(sum(T1_ints))]

    # Calculate the 25th, 50th, and 75th percentiles of the list
    p25 = np.percentile(rand_ints, 25)
    p50 = np.percentile(rand_ints, 50)
    p75 = np.percentile(rand_ints, 75)

    return (p25, p50, p75)