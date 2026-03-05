import matplotlib.pyplot as plt
from itertools import cycle
import numpy as np
from random import shuffle
COLORS = ["b", "g", "r", "c", "m", "y", "k"]
def task_func(list_of_lists):
    fig, ax = plt.subplots()
    color_cycle = cycle(COLORS)
    
    for inner_list in list_of_lists:
        if not inner_list:
            continue
        
        # Shuffle the y-values of the inner list
        shuffle(inner_list)
        
        # Generate sequential x-values starting from 1
        x_values = np.arange(1, len(inner_list) + 1)
        
        # Get the next color from the cycle
        color = next(color_cycle)
        
        # Plot the line with the shuffled y-values and sequential x-values
        ax.plot(x_values, inner_list, color=color)
    
    return fig, ax