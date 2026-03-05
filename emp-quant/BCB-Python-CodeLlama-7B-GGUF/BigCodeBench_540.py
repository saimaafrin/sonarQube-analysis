
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import itertools

def task_func(list_of_menuitems, title="Menu Distribution", color="blue", width=1.0):
    # Flatten the list of menu items
    flat_list = list(itertools.chain.from_iterable(list_of_menuitems))

    # Count the occurrences of each item
    counts = Counter(flat_list)

    # Create a histogram plot
    ax = plt.hist(counts.keys(), bins=np.arange(0, len(counts.keys()) + 1), color=color, width=width)

    # Set the x-axis labels
    ax.set_xticks(np.arange(0, len(counts.keys()) + 1))
    ax.set_xticklabels(counts.keys())

    # Set the y-axis label
    ax.set_ylabel("Frequency")

    # Set the title
    ax.set_title(title)

    return ax