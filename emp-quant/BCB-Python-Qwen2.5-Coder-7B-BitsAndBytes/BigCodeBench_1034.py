
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

CATEGORIES = ["Electronics", "Clothing", "Home Decor", "Automotive", "Books"]

def task_func(s1, s2):
    # Ensure the input series have the same index
    s1 = s1.reindex(CATEGORIES)
    s2 = s2.reindex(CATEGORIES)
    
    # Filter out categories where both stores have sales exceeding the threshold
    filtered_categories = CATEGORIES[(s1 > 200) & (s2 > 200)]
    
    if not filtered_categories.empty:
        # Create a bar plot for the filtered categories
        fig, ax = plt.subplots()
        ax.bar(filtered_categories, s1[filtered_categories], label='Store 1')
        ax.bar(filtered_categories, s2[filtered_categories], bottom=s1[filtered_categories], label='Store 2')
        ax.set_xlabel('Categories')
        ax.set_ylabel('Sales')
        ax.set_title('Sales Comparison Between Two Stores')
        ax.legend()
        
        # Calculate the Euclidean distance between the two series
        euclidean_distance = np.sqrt(np.sum((s1[filtered_categories] - s2[filtered_categories]) ** 2))
        
        return ax, euclidean_distance
    else:
        return None, 0.0