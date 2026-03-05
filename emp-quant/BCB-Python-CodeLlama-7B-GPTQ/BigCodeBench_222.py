import math
import numpy as np
import matplotlib.pyplot as plt
def task_func(list_input):
    # Sort the list in ascending order based on the degree value of its elements
    list_sorted = sorted(list_input, key=lambda x: x[1])

    # Calculate the cumulative sum of the sorted list
    list_cumsum = np.cumsum(list_sorted)

    # Draw a line chart of the cumulative sum
    fig, ax = plt.subplots()
    ax.plot(list_cumsum)
    ax.set_xlabel('Index')
    ax.set_ylabel('Cumulative Sum')
    ax.set_title('Cumulative Sum of Sorted List')

    return (list_cumsum, ax)
list_input = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]