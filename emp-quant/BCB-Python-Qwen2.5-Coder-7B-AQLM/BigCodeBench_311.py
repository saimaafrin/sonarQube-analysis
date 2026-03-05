
import numpy as np
import random
from scipy import stats

def task_func(list_of_lists, size=5, seed=0):
    def calculate_statistics(lst):
        if not lst:
            lst = [random.randint(0, 100) for _ in range(size)]
        mean = np.mean(lst)
        median = np.median(lst)
        mode = stats.mode(lst)[0][0]
        return {'mean': mean, 'median': median, 'mode': mode}

    results = {}
    for i, lst in enumerate(list_of_lists):
        results[f'list_{i+1}'] = calculate_statistics(lst)
    return results