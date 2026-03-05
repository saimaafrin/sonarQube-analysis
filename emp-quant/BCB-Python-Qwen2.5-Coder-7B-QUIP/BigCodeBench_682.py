
from collections import Counter
import math

def task_func(nested_dict):
    aggregated_dict = {}
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            aggregated_dict[key] = sum(value.values())
        else:
            aggregated_dict[key] = value
    aggregated_dict = {k: v for k, v in aggregated_dict.items() if k != "ele"}
    aggregated_dict = {k: math.sin(v) for k, v in aggregated_dict.items()}
    return aggregated_dict