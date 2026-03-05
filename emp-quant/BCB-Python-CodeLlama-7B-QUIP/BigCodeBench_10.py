
import numpy as np
import itertools
import random
import statistics

def task_func(T1, RANGE=100):
    if not T1:
        raise statistics.StatisticsError("T1 is empty")
    list_of_ints = [random.randint(0, RANGE) for i in range(sum(T1))]
    mean = statistics.mean(list_of_ints)
    median = statistics.median(list_of_ints)
    mode = statistics.mode(list_of_ints)
    return (mean, median, mode)