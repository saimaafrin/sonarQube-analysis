import numpy as np
import itertools
import random
import statistics
def task_func(T1, RANGE=100):
    if not T1:
        raise statistics.StatisticsError("T1 is empty")
    
    # Convert elements in 'T1' to integers
    int_values = [int(x) for x in T1]
    
    # Calculate the size of the list based on the sum of the integers in 'T1'
    list_size = sum(int_values)
    
    # Create a list of random integers
    random_list = [random.randint(0, RANGE) for _ in range(list_size)]
    
    # Calculate mean, median, and mode
    mean = np.mean(random_list)
    median = np.median(random_list)
    mode = statistics.mode(random_list)
    
    return (mean, median, mode)