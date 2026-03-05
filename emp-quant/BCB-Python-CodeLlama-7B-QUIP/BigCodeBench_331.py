
import bisect
import random

def task_func(num, list_length = 5, min_value = 0, max_value = 0):
    # Generate a list of random integers
    list_of_ints = [random.randint(min_value, max_value) for i in range(list_length)]

    # Insert the new number into the list
    list_of_ints.insert(bisect.bisect_left(list_of_ints, num), num)

    # Sort the list
    list_of_ints.sort()

    return list_of_ints