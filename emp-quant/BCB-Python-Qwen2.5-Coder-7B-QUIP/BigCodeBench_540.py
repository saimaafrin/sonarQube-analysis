
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import itertools

def task_func(list_of_menuitems, title="Menu Distribution", color="blue", width=1.0):
    # Flatten the list of menu items
    flattened_list = list(itertools.chain.from_iterable(list_of_menuitems))
    
    # Count the occurrences of each item
    item_counts = Counter(flattened_list)
    
    # Get the items and their counts
    items = list(item_counts.keys())
    counts = list(item_counts.values())
    
    # Sort the items alphabetically
    sorted_items = sorted(items)
    sorted_counts = [counts[sorted_items.index(item)] for item in sorted_items]
    
    # Plot the histogram
    ax = plt.subplots()[0]
    ax.bar(range(len(sorted_items)), sorted_counts, width=width, color=color)
    ax.set_xlabel("Menu Items")
    ax.set_ylabel("Frequency")
    ax.set_title(title)
    ax.set_xticks(range(len(sorted_items)))
    ax.set_xticklabels(sorted_items, rotation=90)
    
    return ax