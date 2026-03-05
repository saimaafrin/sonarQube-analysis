from random import randint
import matplotlib.pyplot as plt
import numpy as np
def task_func(array_length=100):
    """
    Generate two arrays of random integers and draw a line diagram with the maximum values of the respective elements of the two arrays. Set 'Maximum Values' on its y-axis.
    """
    # Generate two arrays of random integers
    arr1 = np.random.randint(0, 100, size=array_length)
    arr2 = np.random.randint(0, 100, size=array_length)

    # Find the maximum values of the respective elements of the two arrays
    max_val1 = np.max(arr1)
    max_val2 = np.max(arr2)

    # Create a line diagram with the maximum values on the y-axis
    fig, ax = plt.subplots()
    ax.plot([0, 1], [max_val1, max_val2], 'o-')
    ax.set_xlabel('Array Index')
    ax.set_ylabel('Maximum Value')
    ax.set_title('Maximum Values of Two Arrays')
    ax.grid(True)

    return ax
array_length = 100