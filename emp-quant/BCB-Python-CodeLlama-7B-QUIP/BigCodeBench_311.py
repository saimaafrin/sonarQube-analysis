
import numpy as np
import random
from scipy import stats

def task_func(list_of_lists, size=5, seed=0):
    if not list_of_lists:
        list_of_lists = [random.randint(0, 100) for _ in range(size)]
    return {
        "mean": stats.mean(list_of_lists),
        "median": stats.median(list_of_lists),
        "mode": stats.mode(list_of_lists)
    }