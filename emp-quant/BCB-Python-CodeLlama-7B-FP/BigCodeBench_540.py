from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import itertools
def task_func(list_of_menuitems, title="Menu Distribution", color="blue", width=1.0):
    """
    Given a nested list of menu items, flatten the list using itertools.chain, count the occurrences of each item, then plot a histogram with an alphabetically sorted x-axis labeled as "Menu Items" and y-axis as "Frequency".
    """
    # Flatten the list of menu items using itertools.chain
    flattened_list = list(itertools.chain.from_iterable(list_of_menuitems))

    # Count the occurrences of each item in the flattened list
    item_counts = Counter(flattened_list)

    # Create a histogram of the item counts
    ax = plt.hist(item_counts.values(), bins=np.arange(len(item_counts.keys())), color=color, width=width)

    # Set the x-axis labels to the menu items in alphabetical order
    ax.set_xticks(np.arange(len(item_counts.keys())))
    ax.set_xticklabels(sorted(item_counts.keys()))

    # Set the y-axis label to "Frequency"
    ax.set_ylabel("Frequency")

    # Set the title of the plot
    ax.set_title(title)

    return ax
list_of_menuitems = [
    ["Apple", "Banana", "Cherry"],
    ["Orange", "Grape", "Lemon"],
    ["Pear", "Strawberry", "Mango"]
]