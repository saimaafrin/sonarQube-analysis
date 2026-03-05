
import math
import numpy as np
import matplotlib.pyplot as plt

def task_func(list_input):
    # Sort the list in ascending order based on the degree value of its elements
    sorted_list = sorted(list_input, key=lambda x: x[1])

    # Calculate the cumulative sum of the sorted list
    cumulative_sum = np.cumsum(sorted_list)

    # Plot the line chart of the cumulative sum
    fig, ax = plt.subplots()
    ax.plot(cumulative_sum)
    ax.set_xlabel("Cumulative sum")
    ax.set_ylabel("Value")
    ax.set_title("Cumulative sum of sorted list")
    return cumulative_sum, ax