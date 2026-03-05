
import numpy as np
import random

def task_func(my_list):
    # Append a random integer between 0 and 100 to the list
    my_list.append(random.randint(0, 100))

    # Calculate the sum of the integers in the list
    sum_of_ints = sum(my_list)

    # Create a numpy array of random floating-point numbers
    # with the same length as the sum of the integers in the list
    arr = np.random.rand(sum_of_ints)

    return arr