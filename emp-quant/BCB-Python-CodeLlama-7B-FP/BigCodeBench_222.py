import math
import numpy as np
import matplotlib.pyplot as plt
def task_func(list_input):
    # Sort the list in ascending order based on the degree value of its elements
    sorted_list = sorted(list_input, key=lambda x: x[1])

    # Calculate the cumulative sum of the sorted list
    cumulative_sum = np.cumsum(sorted_list)

    # Draw a line chart of the cumulative sum
    fig, ax = plt.subplots()
    ax.plot(cumulative_sum)
    ax.set_xlabel('Index')
    ax.set_ylabel('Cumulative Sum')
    ax.set_title('Cumulative Sum of Sorted List')
    plt.show()

    return cumulative_sum, ax
list_input = [(1, 2), (2, 3), (3, 1), (4, 4), (5, 5)]