
import heapq
import random

def task_func(obj_list, attr, top_n=5, seed=None):
    if seed is not None:
        random.seed(seed)
    
    # Extract the attribute values from the object list
    values = [getattr(obj, attr) for obj in obj_list if hasattr(obj, attr)]
    
    # Find the top N values using heapq.nlargest
    top_values = heapq.nlargest(top_n, values)
    
    # Randomly sample a value from all attributes
    random_value = random.choice(values) if values else None
    
    return top_values, random_value

random.seed(2)
obj_list = [Object(random.randint(1, 12)) for _ in range(13)]
top_values, random_value = task_func(obj_list, 'test', 2, 12)
print(top_values)  # Output: [12, 11]
print(random_value)  # Output: 5