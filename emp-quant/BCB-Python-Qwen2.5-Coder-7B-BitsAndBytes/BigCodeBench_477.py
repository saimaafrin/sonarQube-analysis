
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(N=100, CATEGORIES=["A", "B", "C", "D", "E"], seed=42):
    # Set the seed for reproducibility
    np.random.seed(seed)
    
    # Generate random values for 'x' and 'y'
    x = np.random.rand(N)
    y = np.random.rand(N)
    
    # Determine the number of unique categories needed
    num_categories = min(len(CATEGORIES), N)
    
    # Randomly sample categories with replacement if N >= len(CATEGORIES),
    # otherwise sample without replacement
    if N >= len(CATEGORIES):
        categories = np.random.choice(CATEGORIES, size=N, replace=True)
    else:
        categories = np.random.choice(CATEGORIES, size=num_categories, replace=False)
        categories = np.repeat(categories, N // num_categories)[:N]
    
    # Create the DataFrame
    df = pd.DataFrame({'x': x, 'y': y, 'category': categories})
    
    # Draw the scatter plot
    fig, ax = plt.subplots()
    for category in CATEGORIES:
        subset = df[df['category'] == category]
        ax.scatter(subset['x'], subset['y'], label=category)
    
    ax.legend()
    plt.show()
    
    return df, ax