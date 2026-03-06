
import pandas as pd
import seaborn as sns
import numpy as np

# Constants
LABELS = ['H\u2082O', 'O\u2082', 'CO\u2082', 'N\u2082', 'Ar']

def task_func(x, y, labels):
    # Create a DataFrame from the input arrays
    data = {'x': x, 'y': y}
    df = pd.DataFrame(data)
    
    # Pivot the DataFrame to create a matrix suitable for the heatmap
    pivot_df = df.pivot_table(index='x', columns='y', aggfunc='size', fill_value=0)
    
    # Create the heatmap using seaborn
    ax = sns.heatmap(pivot_df, annot=True, fmt='d', cmap='YlGnBu')
    
    return ax, df