
import random
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt

def task_func(length, range_limit=100, seed=0):
    if range_limit <= 1:
        raise ValueError("Range limit must be greater than 1")
    random_numbers = [random.randint(1, range_limit) for i in range(length)]
    sorted_numbers = sorted(random_numbers)
    hist, ax = sns.histplot(sorted_numbers, bins=range_limit)
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.set_title("Histogram of random numbers")
    return ax, random_numbers