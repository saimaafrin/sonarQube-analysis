
import numpy as np
import itertools
import random
import statistics

def task_func(T1, RANGE=100):
    if not T1:
        raise statistics.StatisticsError("T1 is empty")
    
    # Convert elements in 'T1' to integers
    int_T1 = [int(x) for x in T1]
    
    # Calculate the total size of the list
    total_size = sum(int_T1)
    
    # Create a list of random integers
    random_list = [random.randint(0, RANGE) for _ in range(total_size)]
    
    # Calculate mean, median, and mode
    mean = np.mean(random_list)
    median = np.median(random_list)
    mode = statistics.mode(random_list)
    
    return (mean, median, mode)