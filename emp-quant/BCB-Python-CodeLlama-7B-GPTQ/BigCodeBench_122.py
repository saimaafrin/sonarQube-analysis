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

    # Create a numpy array of random floating-point numbers with the same size as the sum of the numbers in the list
    random_array = np.random.rand(sum_of_numbers)

    return random_array
my_list = [1, 2, 3, 4, 5]