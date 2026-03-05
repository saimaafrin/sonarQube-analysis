
from collections import Counter
import math

def task_func(nested_dict):
    aggregated_dict = {}
    for key, value in nested_dict.items():
        if key == "ele":
            continue
        if key not in aggregated_dict:
            aggregated_dict[key] = 0
        aggregated_dict[key] += value
    
    result_dict = {key: math.sin(value) for key, value in aggregated_dict.items()}
    return result_dict