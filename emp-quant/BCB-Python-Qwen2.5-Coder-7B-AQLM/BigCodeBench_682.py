
from collections import Counter
import math

def task_func(nested_dict):
    aggregated_dict = Counter()
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            aggregated_dict += task_func(value)
        else:
            aggregated_dict[key] += value
    
    result_dict = {key: math.sin(value) for key, value in aggregated_dict.items()}
    return result_dict