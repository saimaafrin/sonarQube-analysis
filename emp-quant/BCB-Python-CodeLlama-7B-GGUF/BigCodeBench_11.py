
import numpy as np
import itertools
import random

def task_func(T1, max_value=100):
    # Convert elements in T1 to integers
    T1_int = tuple(map(int, T1))

    # Create a list of random integers
    random_list = list(itertools.islice(random.randint(1, max_value), sum(T1_int)))

    # Calculate the 25th, 50th, and 75th percentiles
    p25 = np.percentile(random_list, 25)
    p50 = np.percentile(random_list, 50)
    p75 = np.percentile(random_list, 75)

    return (p25, p50, p75)