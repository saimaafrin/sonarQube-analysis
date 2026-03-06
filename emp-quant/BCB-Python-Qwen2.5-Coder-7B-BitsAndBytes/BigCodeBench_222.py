
import math
import numpy as np
import matplotlib.pyplot as plt

def task_func(list_input):
    # Calculate the degree (number of digits) for each element in the list
    degrees = [len(str(abs(x))) for x in list_input]
    
    # Sort the list based on the degree values
    sorted_list = sorted(list_input, key=lambda x: degrees[list_input.index(x)])
    
    # Calculate the cumulative sum of the sorted list
    cumulative_sum = np.cumsum(sorted_list)
    
    # Create a line chart of the cumulative sum
    fig, ax = plt.subplots()
    ax.plot(cumulative_sum)
    ax.set_xlabel('Index')
    ax.set_ylabel('Cumulative Sum')
    ax.set_title('Line Chart of Cumulative Sum')
    
    return cumulative_sum, ax