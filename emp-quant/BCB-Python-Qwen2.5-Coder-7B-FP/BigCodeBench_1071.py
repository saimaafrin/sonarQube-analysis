import matplotlib.pyplot as plt
from itertools import cycle
import numpy as np
from random import shuffle
COLORS = ["b", "g", "r", "c", "m", "y", "k"]
def task_func(list_of_lists):
    fig, ax = plt.subplots()
    color_cycle = cycle(COLORS)
    
    for y_values in list_of_lists:
        if not y_values:
            continue
        
        shuffle(y_values)
        x_values = np.arange(1, len(y_values) + 1)
        color = next(color_cycle)
        ax.plot(x_values, y_values, color=color)
    
    return fig, ax