
import bisect
import random

def task_func(num, list_length=5, min_value=0, max_value=100):
    # Generate a random sorted list
    if min_value == max_value:
        raise ValueError("min_value must be less than max_value")
    
    random_list = [random.randint(min_value, max_value) for _ in range(list_length)]
    random_list.sort()
    
    # Insert the number using binary search to maintain sorted order
    bisect.insort(random_list, num)
    
    return (random_list[:list_length], random_list)