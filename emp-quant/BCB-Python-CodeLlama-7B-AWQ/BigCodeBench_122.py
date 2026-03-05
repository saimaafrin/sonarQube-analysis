import numpy as np
import random
def task_func(my_list):
    """
    Appends a randomly selected integer between 0 and 100 to the given list 'my_list' and returns a numpy array of random floating-point numbers. The size of the returned array is equal to the sum of the numbers in the modified list.
    """
    # Append a random integer between 0 and 100 to the list
    my_list.append(random.randint(0, 100))

    # Calculate the sum of the numbers in the list
    sum_of_numbers = sum(my_list)

    # Create a numpy array of random floating-point numbers
    array = np.random.rand(sum_of_numbers)

    return array
my_list = [1, 2, 3]