
import bisect
import random

def task_func(num, list_length=5, min_value=0, max_value=0):
    # Generate a random sorted list of integers
    random_list = [random.randint(min_value, max_value) for _ in range(list_length)]
    random_list.sort()
    
    # Insert the number into the sorted list
    bisect.insort(random_list, num)
    
    # Return the original list and the new sorted list as a tuple
    return (random_list, random_list)