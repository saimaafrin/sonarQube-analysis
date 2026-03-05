
import random
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt

def task_func(length, range_limit=100, seed=0):
    if range_limit <= 1:
        raise ValueError("range_limit must be greater than 1")
    
    random.seed(seed)
    random_numbers = [random.randint(0, range_limit - 1) for _ in range(length)]
    
    sns.set()
    axes = sns.histplot(random_numbers, kde=False)
    plt.show()
    
    return axes, random_numbers