
import numpy as np
import random
from scipy import stats

def task_func(list_of_lists, size=5, seed=0):
    def calculate_statistics(lst):
        if not lst:
            return None
        return {
            'mean': np.mean(lst),
            'median': np.median(lst),
            'mode': stats.mode(lst)[0][0] if len(stats.mode(lst)[0]) > 0 else None
        }

    results = []
    for lst in list_of_lists:
        if not lst:
            random.seed(seed)
            lst = [random.randint(0, 100) for _ in range(size)]
        results.append(calculate_statistics(lst))

    return results