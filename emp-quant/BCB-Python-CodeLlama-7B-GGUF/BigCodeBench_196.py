
import random
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt

def task_func(length, range_limit=100, seed=0):
    if range_limit <= 1:
        raise ValueError("Range limit must be greater than 1")

    random.seed(seed)
    numbers = [random.randint(1, range_limit) for _ in range(length)]
    numbers.sort()

    fig, ax = plt.subplots()
    sns.histplot(data=numbers, ax=ax)

    return ax, numbers