
from random import randint
import matplotlib.pyplot as plt
import numpy as np

def task_func(array_length=100):
    # Generate two arrays of random integers
    array1 = [randint(1, 100) for _ in range(array_length)]
    array2 = [randint(1, 100) for _ in range(array_length)]

    # Calculate the maximum values of the respective elements
    max_values = [max(a, b) for a, b in zip(array1, array2)]

    # Create a figure and an axes.
    fig, ax = plt.subplots()

    # Plot the maximum values
    ax.plot(max_values)

    # Set the title and labels
    ax.set_title('Line Diagram of Maximum Values')
    ax.set_xlabel('Index')
    ax.set_ylabel('Maximum Values')

    return ax