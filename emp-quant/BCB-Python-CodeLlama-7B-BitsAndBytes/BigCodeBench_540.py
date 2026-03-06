
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import itertools

def task_func(list_of_menuitems, title="Menu Distribution", color="blue", width=1.0):
    # Flatten the list of menu items using itertools.chain
    flattened_list = list(itertools.chain.from_iterable(list_of_menuitems))

    # Count the occurrences of each item in the flattened list
    counts = Counter(flattened_list)

    # Create a histogram plot with an alphabetically sorted x-axis and a y-axis labeled as "Frequency"
    ax = plt.hist(counts.keys(), bins=np.arange(min(counts.keys()), max(counts.keys()) + 1), color=color, width=width)
    ax.set_xlabel("Menu Items")
    ax.set_ylabel("Frequency")
    ax.set_title(title)

    return ax

ax = task_func(list_of_menuitems, title="Menu Distribution", color="blue", width=1.0)
plt.show()