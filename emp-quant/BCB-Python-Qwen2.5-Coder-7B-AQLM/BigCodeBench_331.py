
import bisect
import random

def task_func(num, list_length=5, min_value=0, max_value=0):
    if max_value == 0:
        max_value = num + 10  # Default max_value if not specified
    
    # Generate a sorted list of random integers
    random_list = sorted(random.sample(range(min_value, max_value), list_length))
    
    # Insert the number into the sorted list
    bisect.insort(random_list, num)
    
    return random_list, random_list