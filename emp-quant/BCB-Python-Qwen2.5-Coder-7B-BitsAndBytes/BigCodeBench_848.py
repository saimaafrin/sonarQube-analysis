
import heapq
import random

class Object:
    def __init__(self, value):
        self.test = value

def task_func(obj_list, attr, top_n=5, seed=None):
    if seed is not None:
        random.seed(seed)
    
    # Extract the attribute values from the object list
    attr_values = [getattr(obj, attr) for obj in obj_list if hasattr(obj, attr)]
    
    # Check if there are any attribute values
    if not attr_values:
        return [], None
    
    # Find the top N values using heapq.nlargest
    top_values = heapq.nlargest(top_n, attr_values)
    
    # Randomly sample one value from all attribute values
    random_value = random.choice(attr_values)
    
    return top_values, random_value