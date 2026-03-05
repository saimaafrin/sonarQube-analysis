
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import itertools

def task_func(list_of_menuitems, title="Menu Distribution", color="blue", width=1.0):
    # Flatten the list using itertools.chain
    flattened_list = itertools.chain.from_iterable(list_of_menuitems)
    # Count the occurrences of each item in the flattened list
    counter = Counter(flattened_list)
    # Sort the counter by key (item) and value (count)
    sorted_counter = sorted(counter.items(), key=lambda x: x[0], value=x[1])
    # Create a histogram with an alphabetically sorted x-axis and a y-axis
    ax = plt.hist(np.arange(len(sorted_counter)), bins=len(sorted_counter), color=color, width=width)
    # Set the x-axis labels to the menu items
    ax.set_xticks(np.arange(len(sorted_counter)))
    ax.set_xticklabels(sorted_counter.keys())
    # Set the y-axis labels to the frequency of each item
    ax.set_yticks(np.arange(len(sorted_counter)))
    ax.set_yticklabels(sorted_counter.values())
    return ax