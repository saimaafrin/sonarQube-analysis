
import matplotlib.pyplot as plt
from itertools import cycle
import numpy as np
from random import shuffle

COLORS = ["b", "g", "r", "c", "m", "y", "k"]

def task_func(list_of_lists):
    fig, ax = plt.subplots()
    for i, inner_list in enumerate(list_of_lists):
        if not inner_list:
            continue
        shuffled_y = np.random.rand(len(inner_list))
        shuffled_x = np.arange(1, len(inner_list) + 1)
        ax.plot(shuffled_x, shuffled_y, color=COLORS[i % len(COLORS)])
    return fig, ax