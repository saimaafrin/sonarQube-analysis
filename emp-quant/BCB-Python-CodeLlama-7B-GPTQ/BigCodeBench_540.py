from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import itertools
def task_func(list_of_menuitems, title="Menu Distribution", color="blue", width=1.0):
    """
    Given a nested list of menu items, flatten the list using itertool chain, count the occurrences of each item, then plot a histogram with an alphabetically sorted x-axis labeled as "Menu Items" and y-axis as "Frequency".
    """
    # Flatten the list of menu items using itertools.chain
    flattened_list = list(itertools.chain.from_iterable(list_of_menuitems))

    # Count the occurrences of each item in the flattened list
    item_counts = Counter(flattened_list)

    # Create a numpy array of the item counts
    item_counts_array = np.array(list(item_counts.values()))

    # Create a numpy array of the item names
    item_names = np.array(list(item_counts.keys()))

    # Sort the item names alphabetically
    item_names.sort()

    # Create a histogram plot with the item names on the x-axis and the item counts on the y-axis
    ax = plt.bar(item_names, item_counts_array, color=color, width=width)

    # Set the title of the plot
    ax.set_title(title)

    # Set the x-axis label
    ax.set_xlabel("Menu Items")

    # Set the y-axis label
    ax.set_ylabel("Frequency")

    # Return the Axes object representing the histogram plot
    return ax
list_of_menuitems = [
    ["Apple", "Orange", "Banana"],
    ["Coffee", "Tea", "Milk"],
    ["Sandwich", "Pizza", "Salad"]
]