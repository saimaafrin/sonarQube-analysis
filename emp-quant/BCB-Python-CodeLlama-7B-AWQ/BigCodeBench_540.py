from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import itertools
def task_func(list_of_menuitems, title="Menu Distribution", color="blue", width=1.0):
    """
    Given a nested list of menu items, flatten the list using itertool chain, count the occurrences of each item, then plot a histogram with an alphabetically sorted x-axis labeled as "Menu Items" and y-axis as "Frequency".
    """
    # Flatten the list using itertools.chain
    flattened_list = list(itertools.chain.from_iterable(list_of_menuitems))

    # Count the occurrences of each item
    counter = Counter(flattened_list)

    # Create a histogram with an alphabetically sorted x-axis labeled as "Menu Items" and y-axis as "Frequency"
    ax = plt.hist(counter.keys(), bins=np.arange(len(counter.keys())), color=color, width=width)
    ax.set_xlabel("Menu Items")
    ax.set_ylabel("Frequency")
    ax.set_title(title)

    return ax
list_of_menuitems = [
    ["Apple", "Orange", "Banana"],
    ["Orange", "Grapes", "Mango"],
    ["Banana", "Mango", "Pear"]
]