
import matplotlib.pyplot as plt
from itertools import cycle
import numpy as np
from random import shuffle

COLORS = ["b", "g", "r", "c", "m", "y", "k"]

def task_func(list_of_lists):
    fig, ax = plt.subplots()
    color_cycle = cycle(COLORS)
    for i, inner_list in enumerate(list_of_lists):
        if not inner_list:
            continue
        shuffled_y = np.random.permutation(inner_list)
        ax.plot(np.arange(1, len(inner_list) + 1), shuffled_y, color=next(color_cycle))
    return fig, ax