
from random import randint
import matplotlib.pyplot as plt
import numpy as np

def task_func(array_length=100):
    # Generate two arrays of random integers
    arr1 = np.random.randint(0, 100, size=array_length)
    arr2 = np.random.randint(0, 100, size=array_length)

    # Find the maximum values of the respective elements of the two arrays
    max_val1 = np.max(arr1)
    max_val2 = np.max(arr2)

    # Create a line diagram with the maximum values on the y-axis
    fig, ax = plt.subplots()
    ax.plot(arr1, arr2)
    ax.set_ylabel('Maximum Values')
    ax.set_xlabel('Array Elements')
    ax.set_title('Maximum Values of Array Elements')
    ax.set_ylim([0, max_val1 + max_val2])

    return ax