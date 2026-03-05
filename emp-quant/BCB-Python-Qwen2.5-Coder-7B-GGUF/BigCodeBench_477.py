
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(N=100, CATEGORIES=["A", "B", "C", "D", "E"], seed=42):
    np.random.seed(seed)
    
    # Ensure each category appears at least once if N >= len(CATEGORIES)
    if N >= len(CATEGORIES):
        categories = np.array(CATEGORIES)
    else:
        categories = np.random.choice(CATEGORIES, N, replace=False)
    
    # Generate random values for 'x' and 'y'
    x = np.random.rand(N)
    y = np.random.rand(N)
    
    # Create DataFrame
    df = pd.DataFrame({'x': x, 'y': y, 'category': categories})
    
    # Draw scatter plot
    fig, ax = plt.subplots()
    for category in CATEGORIES:
        subset = df[df['category'] == category]
        ax.scatter(subset['x'], subset['y'], label=category)
    
    ax.legend()
    plt.show()
    
    return df, ax