from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import itertools
def task_func(list_of_menuitems, title="Menu Distribution", color="blue", width=1.0):
    # Flatten the nested list using itertools.chain
    flattened_list = list(itertools.chain.from_iterable(list_of_menuitems))
    
    # Count the occurrences of each item
    item_counts = Counter(flattened_list)
    
    # Sort items alphabetically
    sorted_items = sorted(item_counts.keys())
    
    # Extract counts for sorted items
    counts = [item_counts[item] for item in sorted_items]
    
    # Create a figure and axis for the plot
    fig, ax = plt.subplots()
    
    # Plot the histogram
    ax.bar(sorted_items, counts, color=color, width=width)
    
    # Set the title and labels
    ax.set_title(title)
    ax.set_xlabel("Menu Items")
    ax.set_ylabel("Frequency")
    
    # Return the Axes object
    return ax