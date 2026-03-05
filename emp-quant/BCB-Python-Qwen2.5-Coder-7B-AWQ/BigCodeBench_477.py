import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def task_func(N=100, CATEGORIES=["A", "B", "C", "D", "E"], seed=42):
    """
    Generates a DataFrame with N rows and 3 columns ('x', 'y', 'category') and plots a scatter plot.
    
    Parameters:
    - N: Number of rows in the DataFrame.
    - CATEGORIES: List of categories to be used in the 'category' column.
    - seed: Seed for random number generation.
    
    Returns:
    - A tuple containing:
        - DataFrame: The generated DataFrame.
        - Axes: The Axes object of the scatter plot.
    """
    np.random.seed(seed)
    
    # Generate random values for 'x' and 'y'
    df = pd.DataFrame({
        'x': np.random.rand(N),
        'y': np.random.rand(N)
    })
    
    # Determine the number of categories to use
    num_categories = min(N, len(CATEGORIES))
    
    # Assign random categories to each row
    if N >= len(CATEGORIES):
        df['category'] = np.random.choice(CATEGORIES, N, replace=True)
    else:
        df['category'] = np.random.choice(CATEGORIES, N, replace=False)
    
    # Plot the scatter plot
    fig, ax = plt.subplots()
    for category in CATEGORIES:
        subset = df[df['category'] == category]
        ax.scatter(subset['x'], subset['y'], label=category)
    
    ax.legend()
    plt.show()
    
    return df, ax