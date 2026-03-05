
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import itertools

def task_func(list_of_menuitems, title="Menu Distribution", color="blue", width=1.0):
    # Flatten the nested list using itertools.chain
    flattened_list = list(itertools.chain.from_iterable(list_of_menuitems))
    
    # Count the occurrences of each item
    item_counts = Counter(flattened_list)
    
    # Prepare data for plotting
    menu_items = sorted(item_counts.keys())
    frequencies = [item_counts[item] for item in menu_items]
    
    # Create a histogram plot
    ax = plt.figure(figsize=(10, 6)).add_subplot(111)
    ax.bar(menu_items, frequencies, color=color, width=width)
    
    # Set the title and labels
    ax.set_title(title)
    ax.set_xlabel("Menu Items")
    ax.set_ylabel("Frequency")
    
    # Show the plot
    plt.show()
    
    return ax