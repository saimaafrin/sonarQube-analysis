
import numpy as np
import random

def task_func(my_list):
    # Append a random integer between 0 and 100 to the list
    my_list.append(random.randint(0, 100))

    # Create a numpy array of random floating-point numbers
    # with the size equal to the sum of the integers in the modified list
    array = np.random.rand(sum(my_list))

    return array