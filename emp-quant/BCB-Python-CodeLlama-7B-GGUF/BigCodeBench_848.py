
import heapq
import random

def task_func(obj_list, attr, top_n=5, seed=None):
    if not obj_list:
        return [], None

    if seed is not None:
        random.seed(seed)

    top_values = []
    for obj in obj_list:
        if hasattr(obj, attr):
            top_values.append(getattr(obj, attr))

    if not top_values:
        return [], None

    top_values = sorted(top_values, reverse=True)[:top_n]

    random_value = random.choice(top_values) if top_values else None

    return top_values, random_value