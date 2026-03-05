import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
CATEGORIES = ["Electronics", "Clothing", "Home Decor", "Automotive", "Books"]
def task_func(s1, s2):
    # Filter categories where both stores have sales exceeding the threshold of 200
    filtered_categories = [category for category in CATEGORIES if s1[category] > 200 and s2[category] > 200]
    
    if not filtered_categories:
        return None, 0.0
    
    # Prepare data for plotting
    sales_data = {
        'Category': filtered_categories,
        'Store 1': [s1[category] for category in filtered_categories],
        'Store 2': [s2[category] for category in filtered_categories]
    }
    
    # Create a bar plot
    fig, ax = plt.subplots()
    bar_width = 0.35
    index = np.arange(len(filtered_categories))
    
    bars1 = ax.bar(index, sales_data['Store 1'], bar_width, label='Store 1')
    bars2 = ax.bar(index + bar_width, sales_data['Store 2'], bar_width, label='Store 2')
    
    ax.set_xlabel('Category')
    ax.set_ylabel('Sales')
    ax.set_title('Sales Comparison Between Two Stores')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(sales_data['Category'])
    ax.legend()
    
    plt.show()
    
    # Calculate Euclidean distance
    sales_series1 = pd.Series(sales_data['Store 1'], index=sales_data['Category'])
    sales_series2 = pd.Series(sales_data['Store 2'], index=sales_data['Category'])
    euclidean_distance = np.linalg.norm(sales_series1 - sales_series2)
    
    return ax, euclidean_distance