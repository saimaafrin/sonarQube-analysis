
import seaborn as sns
from random import sample
import pandas as pd
import matplotlib.pyplot as plt

# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def task_func(df, tuples, n_plots):
    # Remove rows based on the specified tuples
    df = df[~df.isin(tuples).all(axis=1)]
    
    # Generate random pairs of columns and create pairplots
    fig, axes = plt.subplots(n_plots, 2, figsize=(12, n_plots*4))
    axes = axes.flatten()
    
    # Ensure the number of plots is less than or equal to the number of pairs
    n_plots = min(n_plots, len(COLUMNS) * (len(COLUMNS) - 1) // 2)
    
    for ax, (i, j) in zip(axes, sample(list(zip(COLUMNS, COLUMNS)), n_plots)):
        sns.scatterplot(x=i, y=j, data=df, ax=ax)
        ax.set_title(f'{i} vs {j}')
    
    plt.tight_layout()
    plt.show()
    
    return df, axes

    # Tuples to remove
    tuples_to_remove = [(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)]
    
    # Generate plots
    modified_df, axes = task_func(df, tuples_to_remove, 5)
    
    # Output the modified DataFrame
    print(modified_df)