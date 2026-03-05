import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
CATEGORIES = ["Electronics", "Clothing", "Home Decor", "Automotive", "Books"]
def task_func(s1, s2):
    # Filter categories where both stores have sales exceeding the threshold of 200
    filtered_categories = [category for category in CATEGORIES if s1[category] > 200 and s2[category] > 200]
    
    # If no categories meet the threshold, return None for the plot and 0.0 for the distance
    if not filtered_categories:
        return None, 0.0
    
    # Create a bar plot for the filtered categories
    fig, ax = plt.subplots()
    ax.bar(filtered_categories, [s1[category] for category in filtered_categories], label='Store 1')
    ax.bar(filtered_categories, [s2[category] for category in filtered_categories], bottom=[s1[category] for category in filtered_categories], label='Store 2')
    ax.set_xlabel('Categories')
    ax.set_ylabel('Sales')
    ax.set_title('Sales Comparison Between Two Stores')
    ax.legend()
    
    # Calculate the Euclidean distance between the two series for the filtered categories
    distance = np.sqrt(sum((s1[category] - s2[category]) ** 2 for category in filtered_categories))
    
    return ax, distance