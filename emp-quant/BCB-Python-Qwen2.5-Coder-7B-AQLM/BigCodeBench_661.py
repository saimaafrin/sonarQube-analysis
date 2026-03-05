
import pandas as pd
import seaborn as sns
import numpy as np

# Constants
LABELS = ['H\u2082O', 'O\u2082', 'CO\u2082', 'N\u2082', 'Ar']

def task_func(x, y, labels):
    # Create a DataFrame with the provided x, y, and labels
    df = pd.DataFrame({'x': x, 'y': y, 'labels': labels})
    
    # Pivot the DataFrame to create a matrix for the heatmap
    pivot_df = df.pivot(index='x', columns='y', values='labels')
    
    # Create a heatmap using seaborn
    ax = sns.heatmap(pivot_df, annot=True, fmt='s', cmap='viridis')
    
    return ax, df