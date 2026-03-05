import bisect
import random
def task_func(num, list_length=5, min_value=0, max_value=0):
    # Generate a random sorted list of integers
    if min_value == 0 and max_value == 0:
        random_list = sorted(random.sample(range(1, 100), list_length))
    else:
        random_list = sorted(random.sample(range(min_value, max_value + 1), list_length))
    
    # Insert the number into the sorted list
    bisect.insort(random_list, num)
    
    # Return the original and new sorted list as a tuple
    return (random_list, random_list)