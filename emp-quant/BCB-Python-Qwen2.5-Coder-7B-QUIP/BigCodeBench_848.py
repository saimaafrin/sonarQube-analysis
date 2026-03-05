
import heapq
import random

def task_func(obj_list, attr, top_n=5, seed=None):
    # Extract the values of the specified attribute from the objects
    values = [getattr(obj, attr) for obj in obj_list]
    
    # Filter out non-integer values
    values = [v for v in values if isinstance(v, int)]
    
    # If there are no valid integer values, return an empty list and None
    if not values:
        return [], None
    
    # Find the top N values using a heap
    top_values = heapq.nlargest(top_n, values)
    
    # Shuffle the list of values and select one randomly
    random_value = random.choice(values)
    
    return top_values, random_value