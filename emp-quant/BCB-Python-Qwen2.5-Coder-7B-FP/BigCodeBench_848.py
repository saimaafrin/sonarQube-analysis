import heapq
import random
def task_func(obj_list, attr, top_n=5, seed=None):
    if seed is not None:
        random.seed(seed)
    
    # Extract the attribute values from the list of objects
    values = [getattr(obj, attr) for obj in obj_list if hasattr(obj, attr)]
    
    # Check if there are any values to process
    if not values:
        return [], None
    
    # Find the top N values using heapq.nlargest
    top_values = heapq.nlargest(top_n, values)
    
    # Randomly sample a value from all attributes
    random_value = random.choice(values)
    
    return top_values, random_value
obj_list = [Object(random.randint(1, 12)) for _ in range(13)]