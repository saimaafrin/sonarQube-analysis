
import heapq
import random

def task_func(obj_list, attr, top_n=5, seed=None):
    if seed is not None:
        random.seed(seed)
    
    # Extract the attribute values from the objects
    attr_values = [getattr(obj, attr) for obj in obj_list if hasattr(obj, attr)]
    
    # Find the top N values
    top_values = heapq.nlargest(top_n, attr_values)
    
    # Randomly sample a value from all attributes
    random_value = random.choice(attr_values) if attr_values else None
    
    return top_values, random_value