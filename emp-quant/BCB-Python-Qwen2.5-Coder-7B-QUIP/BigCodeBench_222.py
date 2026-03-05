
import math
import numpy as np
import matplotlib.pyplot as plt

def task_func(list_input):
    # Sort the list based on the degree value of its elements
    sorted_list = sorted(list_input, key=lambda x: math.deg(x))
    
    # Calculate the cumulative sum of the sorted list
    cumulative_sum = np.cumsum(sorted_list)
    
    # Draw a line chart of the cumulative sum
    fig, ax = plt.subplots()
    ax.plot(cumulative_sum, 'o-')
    
    # Return the tuple containing the numpy array and the Axes object
    return cumulative_sum, ax