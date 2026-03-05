
import pandas as pd
import seaborn as sns
import numpy as np
# Constants
LABELS = ['H\u2082O', 'O\u2082', 'CO\u2082', 'N\u2082', 'Ar']

def task_func(x, y, labels):
    # Create a DataFrame with the given x and y values
    df = pd.DataFrame({'x': x, 'y': y})
    
    # Pivot the DataFrame to create a matrix for the heatmap
    heatmap_data = df.pivot(index='x', columns='y', values='y')
    
    # Create a heatmap using seaborn
    ax = sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='viridis', cbar_kws={'label': 'Value'})
    
    # Set the labels for the x and y axes
    ax.set_xlabel('X Values')
    ax.set_ylabel('Y Values')
    
    # Set the tick labels to the provided labels
    ax.set_xticklabels(labels)
    ax.set_yticklabels(labels)
    
    return ax, df