import math
import numpy as np
import matplotlib.pyplot as plt
def task_func(list_input):
    # Calculate the degree value of each element in the list
    degrees = [math.degrees(math.atan2(y, x)) for x, y in list_input]
    
    # Sort the list based on the degree value
    sorted_list = sorted(list_input, key=lambda point: degrees[list_input.index(point)])
    
    # Calculate the cumulative sum of the sorted list
    cumulative_sum = np.cumsum(sorted_list)
    
    # Draw a line chart of the cumulative sum
    fig, ax = plt.subplots()
    ax.plot(cumulative_sum)
    
    return cumulative_sum, ax