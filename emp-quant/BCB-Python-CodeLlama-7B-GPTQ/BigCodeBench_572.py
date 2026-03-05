from random import randint
import matplotlib.pyplot as plt
import numpy as np
def task_func(array_length=100):
    """
    Generate two arrays of random integers and draw a line diagram with the maximum values of the respective elements of the two arrays.
    Set 'Maximum Values' on its y-axis.
    """
    # Generate two arrays of random integers
    array1 = np.random.randint(1, 100, size=array_length)
    array2 = np.random.randint(1, 100, size=array_length)

    # Find the maximum values of the respective elements of the two arrays
    max_array1 = np.amax(array1)
    max_array2 = np.amax(array2)

    # Create a line diagram with the maximum values on the y-axis
    fig, ax = plt.subplots()
    ax.plot(max_array1, label='Array 1')
    ax.plot(max_array2, label='Array 2')
    ax.set_ylabel('Maximum Values')
    ax.legend()

    return ax
array_length = 100