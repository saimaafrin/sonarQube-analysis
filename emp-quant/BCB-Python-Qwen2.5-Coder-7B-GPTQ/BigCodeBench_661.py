import pandas as pd
import seaborn as sns
import numpy as np
def task_func(x, y, labels):
    """
    Create a heatmap using seaborn for given x and y values with labels.

    Parameters:
    x (list): A list of x-values.
    y (list): A list of y-values.
    labels (list): A list of labels for the heatmap.

    Returns:
    ax (Axes): A seaborn heatmap object.
    df (DataFrame): The dataframe used to create the heatmap.
    """
    # Create a DataFrame from the input lists
    df = pd.DataFrame({'x': x, 'y': y})
    
    # Pivot the DataFrame to create a matrix suitable for the heatmap
    df_pivot = df.pivot_table(index='y', columns='x', aggfunc='size', fill_value=0)
    
    # Create the heatmap
    ax = sns.heatmap(df_pivot, annot=True, fmt='d', cmap='YlGnBu', cbar_kws={'label': 'Count'})
    
    # Set the labels for the heatmap
    ax.set_xlabel('X Values')
    ax.set_ylabel('Y Values')
    ax.set_title('Heatmap of X and Y Values')
    
    return ax, df_pivot