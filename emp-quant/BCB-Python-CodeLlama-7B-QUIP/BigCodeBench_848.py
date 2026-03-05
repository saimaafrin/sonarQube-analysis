
import heapq
import random

def task_func(obj_list, attr, top_n=5, seed=None):
    if seed:
        random.seed(seed)
    top_values = []
    random_value = None
    for obj in obj_list:
        if hasattr(obj, attr):
            value = getattr(obj, attr)
            if value:
                heapq.heappush(top_values, value)
                if len(top_values) == top_n:
                    random_value = random.choice(top_values)
    return top_values, random_value