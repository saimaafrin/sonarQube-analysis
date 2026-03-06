
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import itertools

def task_func(list_of_menuitems, title="Menu Distribution", color="blue", width=1.0):
    # Flatten the nested list
    flattened_list = list(itertools.chain.from_iterable(list_of_menuitems))
    
    # Count the occurrences of each item
    counter = Counter(flattened_list)
    
    # Sort items alphabetically
    sorted_items = sorted(counter.items())
    
    # Extract labels and values for plotting
    labels, values = zip(*sorted_items)
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot the histogram
    ax.bar(labels, values, color=color, width=width)
    
    # Set the title and labels
    ax.set_title(title)
    ax.set_xlabel("Menu Items")
    ax.set_ylabel("Frequency")
    
    # Rotate x-axis labels for better readability
    ax.tick_params(axis='x', rotation=45)
    
    return ax