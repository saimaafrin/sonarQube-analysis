
import numpy as np
import itertools
import random
import statistics

def task_func(T1, RANGE=100):
    if not T1:
        raise statistics.StatisticsError("T1 is empty")
    
    # Convert elements in T1 to integers
    int_T1 = [int(x) for x in T1]
    
    # Calculate the total number of random integers needed
    total_size = sum(int_T1)
    
    # Generate the list of random integers
    random_list = []
    for num in int_T1:
        random_list.extend(random.sample(range(RANGE), num))
    
    # Calculate mean, median, and mode
    mean_value = np.mean(random_list)
    median_value = np.median(random_list)
    mode_value = statistics.mode(random_list)
    
    return (mean_value, median_value, mode_value)