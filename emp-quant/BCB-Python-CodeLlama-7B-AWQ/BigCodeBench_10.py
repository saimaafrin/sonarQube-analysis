import numpy as np
import itertools
import random
import statistics
def task_func(T1, RANGE=100):
    """
    Convert elements in 'T1' to integers and create a list of random integers.
    The size of the list is the sum of the integers in `T1`.
    Calculate and return the mean, median, and mode of the list.
    The function should raise the exception for: statistics.StatisticsError if T1 is empty
    The function should output with:
        tuple: A tuple containing the mean, median, and mode of the generated list of random integers.
        The mean and median are floats, and the mode is an integer. The calculations use the generated
        list whose size is determined by the sum of converted integers from `T1`.
    """
    if not T1:
        raise statistics.StatisticsError("T1 is empty")

    # Convert elements in 'T1' to integers and create a list of random integers
    T1_int = [int(x) for x in T1]
    rand_list = [random.randint(0, RANGE) for _ in range(sum(T1_int))]

    # Calculate and return the mean, median, and mode of the list
    mean = statistics.mean(rand_list)
    median = statistics.median(rand_list)
    mode = statistics.mode(rand_list)
    return (mean, median, mode)
T1 = ["1", "2", "3"]