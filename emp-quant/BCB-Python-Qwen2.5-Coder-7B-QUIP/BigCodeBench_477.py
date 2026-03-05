
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(N=100, CATEGORIES=["A", "B", "C", "D", "E"], seed=42):
    # Set the seed for reproducibility
    np.random.seed(seed)
    
    # Generate random values for 'x' and 'y'
    x = np.random.rand(N)
    y = np.random.rand(N)
    
    # Determine the number of categories to sample
    num_categories = min(N, len(CATEGORIES))
    
    # Sample categories with replacement if N is less than the number of categories
    categories = np.random.choice(CATEGORIES, size=num_categories, replace=True)
    
    # Create the DataFrame
    df = pd.DataFrame({'x': x, 'y': y, 'category': categories})
    
    # Draw the scatter plot
    fig, ax = plt.subplots()
    for category in CATEGORIES:
        ax.scatter(df[df['category'] == category]['x'], df[df['category'] == category]['y'], label=category)
    ax.legend()
    
    return df, ax