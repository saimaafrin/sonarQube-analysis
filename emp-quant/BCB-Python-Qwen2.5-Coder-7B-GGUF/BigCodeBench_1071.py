
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
        
        x_values = np.arange(1, len(inner_list) + 1)
        y_values = inner_list.copy()
        shuffle(y_values)
        
        color = next(color_cycle)
        ax.plot(x_values, y_values, color=color)
    
    return fig, ax