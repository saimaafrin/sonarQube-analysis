import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def task_func(N=100, CATEGORIES=["A", "B", "C", "D", "E"], seed=42):
    """
    Generates a DataFrame with N rows and 3 columns ('x', 'y', 'category') and plots a scatter plot.
    
    Parameters:
    - N: Number of rows in the DataFrame.
    - CATEGORIES: List of categories to be used in the 'category' column.
    - seed: Seed for random number generation for reproducibility.
    
    Returns:
    - A tuple containing:
        - DataFrame: The generated DataFrame.
        - Axes: The Axes object of the scatter plot.
    """
    # Set the seed for reproducibility
    np.random.seed(seed)
    
    # Generate random values for 'x' and 'y'
    x = np.random.rand(N)
    y = np.random.rand(N)
    
    # Determine the number of categories to use
    num_categories = min(N, len(CATEGORIES))
    
    # Randomly sample categories with replacement if N is greater than or equal to the number of categories
    if N >= len(CATEGORIES):
        categories = np.random.choice(CATEGORIES, size=N, replace=True)
    else:
        # Randomly sample categories without replacement
        categories = np.random.choice(CATEGORIES, size=num_categories, replace=False)
        # Repeat each category to fill the DataFrame
        categories = np.repeat(categories, N // num_categories)
        # Add remaining categories randomly
        remaining = N % num_categories
        categories = np.append(categories, np.random.choice(categories, size=remaining, replace=False))
    
    # Create the DataFrame
    df = pd.DataFrame({'x': x, 'y': y, 'category': categories})
    
    # Plot the scatter plot
    fig, ax = plt.subplots()
    for category in CATEGORIES:
        subset = df[df['category'] == category]
        ax.scatter(subset['x'], subset['y'], label=category)
    
    ax.legend()
    plt.show()
    
    return df, ax