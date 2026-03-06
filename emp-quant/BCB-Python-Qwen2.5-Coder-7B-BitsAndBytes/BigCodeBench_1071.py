
import matplotlib.pyplot as plt
from itertools import cycle
import numpy as np
from random import shuffle

COLORS = ["b", "g", "r", "c", "m", "y", "k"]

def task_func(list_of_lists):
    fig, ax = plt.subplots()
    color_cycle = cycle(COLORS)
    
    for i, lst in enumerate(list_of_lists):
        if not lst:
            continue
        
        # Shuffle the y-values while keeping the corresponding x-values intact
        x_values = np.arange(1, len(lst) + 1)
        y_values = lst.copy()
        shuffle(y_values)
        
        # Plot the line with a unique color
        color = next(color_cycle)
        ax.plot(x_values, y_values, color=color, label=f'List {i+1}')
    
    # Add legend to distinguish between lines
    ax.legend()
    
    return fig, ax