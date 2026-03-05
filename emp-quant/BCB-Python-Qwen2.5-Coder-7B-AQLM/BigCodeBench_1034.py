
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean

CATEGORIES = ["Electronics", "Clothing", "Home Decor", "Automotive", "Books"]

def task_func(s1, s2):
    # Create a DataFrame to store the sales data
    sales_data = pd.DataFrame({'Category': CATEGORIES, 'Store1': s1, 'Store2': s2})
    
    # Filter categories where both stores have sales exceeding the threshold of 200
    filtered_data = sales_data[(sales_data['Store1'] > 200) & (sales_data['Store2'] > 200)]
    
    # Check if there are any categories meeting the threshold
    if filtered_data.empty:
        return None, 0.0
    
    # Create a bar plot for the filtered categories
    fig, ax = plt.subplots()
    ax.bar(filtered_data['Category'], filtered_data['Store1'], label='Store1')
    ax.bar(filtered_data['Category'], filtered_data['Store2'], bottom=filtered_data['Store1'], label='Store2')
    ax.set_xlabel('Category')
    ax.set_ylabel('Sales')
    ax.set_title('Sales Comparison for Categories Exceeding 200')
    ax.legend()
    
    # Compute the Euclidean distance between the two series
    distance = euclidean(filtered_data['Store1'], filtered_data['Store2'])
    
    return ax, distance