
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
CATEGORIES = ["Electronics", "Clothing", "Home Decor", "Automotive", "Books"]

def task_func(s1, s2):
    # Filter categories where both stores have sales exceeding the threshold
    filtered_categories = [category for category in CATEGORIES if s1[category] > 200 and s2[category] > 200]
    
    # Create a bar plot for the filtered categories
    if filtered_categories:
        fig, ax = plt.subplots()
        ax.bar(filtered_categories, [s1[category] for category in filtered_categories], label='Store 1')
        ax.bar([category + '_2' for category in filtered_categories], [s2[category] for category in filtered_categories], label='Store 2')
        ax.set_xlabel('Categories')
        ax.set_ylabel('Sales')
        ax.set_title('Sales Comparison')
        ax.legend()
        plt.show()
        return ax, 0.0
    else:
        return None, 0.0

    # Calculate the Euclidean distance between the two series
    euclidean_distance = np.sqrt(np.sum((s1 - s2) ** 2))
    return ax, euclidean_distance