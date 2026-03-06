
import numpy as np
import itertools
import random
import statistics

def task_func(T1, RANGE=100):
    if not T1:
        raise statistics.StatisticsError("T1 is empty")

    # Convert elements in T1 to integers
    T1_int = [int(x) for x in T1]

    # Calculate the sum of the integers in T1
    sum_T1 = sum(T1_int)

    # Generate a list of random integers
    random_list = [random.randint(1, RANGE) for _ in range(sum_T1)]

    # Calculate the mean, median, and mode of the list
    mean = statistics.mean(random_list)
    median = statistics.median(random_list)
    mode = statistics.mode(random_list)

    return mean, median, mode