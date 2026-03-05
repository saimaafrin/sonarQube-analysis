
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
        
        # Plot the line with the current color
        ax.plot(range(1, len(inner_list) + 1), inner_list, color=next(color_cycle))
    
    return fig, ax