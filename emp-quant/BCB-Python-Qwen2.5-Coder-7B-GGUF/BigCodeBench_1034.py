
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance

CATEGORIES = ["Electronics", "Clothing", "Home Decor", "Automotive", "Books"]

def task_func(s1, s2):
    # Filter categories where both stores have sales exceeding the threshold of 200
    filtered_categories = [category for category in CATEGORIES if s1[category] > 200 and s2[category] > 200]
    
    if not filtered_categories:
        return None, 0.0
    
    # Prepare data for plotting
    sales_s1 = [s1[category] for category in filtered_categories]
    sales_s2 = [s2[category] for category in filtered_categories]
    
    # Create a bar plot
    fig, ax = plt.subplots()
    index = np.arange(len(filtered_categories))
    bar_width = 0.35
    
    rects1 = ax.bar(index, sales_s1, bar_width, label='Store 1')
    rects2 = ax.bar(index + bar_width, sales_s2, bar_width, label='Store 2')
    
    ax.set_xlabel('Categories')
    ax.set_ylabel('Sales')
    ax.set_title('Sales Comparison Between Two Stores')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(filtered_categories)
    ax.legend()
    
    plt.show()
    
    # Calculate Euclidean distance
    euclidean_distance = distance.euclidean(sales_s1, sales_s2)
    
    return ax, euclidean_distance