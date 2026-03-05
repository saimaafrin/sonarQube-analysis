from random import randint
import matplotlib.pyplot as plt
import numpy as np
def task_func(array_length=100):
    """
    Generate two arrays of random integers and draw a line diagram with the maximum values of the respective elements of the two arrays. Set 'Maximum Values' on its y-axis.
    """
    # Generate two arrays of random integers
    array1 = np.random.randint(1, 100, size=array_length)
    array2 = np.random.randint(1, 100, size=array_length)

    # Find the maximum values of the respective elements of the two arrays
    max_val1 = np.max(array1)
    max_val2 = np.max(array2)

    # Create a line diagram with the maximum values on the y-axis
    fig, ax = plt.subplots()
    ax.plot(max_val1, max_val2)
    ax.set_xlabel('Array 1')
    ax.set_ylabel('Array 2')
    ax.set_title('Maximum Values')
    return ax
array_length = 100