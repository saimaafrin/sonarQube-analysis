
import math
import numpy as np
import matplotlib.pyplot as plt

def task_func(list_input):
    # Calculate the degree value of each element in the list
    degrees = [math.degrees(math.atan2(y, x)) for x, y in list_input]
    
    # Sort the list based on the degree value
    sorted_list = [x for _, x in sorted(zip(degrees, list_input))]
    
    # Calculate the cumulative sum of the sorted list
    cumulative_sum = np.cumsum(sorted_list)
    
    # Draw a line chart of the cumulative sum
    fig, ax = plt.subplots()
    ax.plot(cumulative_sum)
    ax.set_xlabel('Index')
    ax.set_ylabel('Cumulative Sum')
    ax.set_title('Cumulative Sum of Sorted List')
    
    return cumulative_sum, ax