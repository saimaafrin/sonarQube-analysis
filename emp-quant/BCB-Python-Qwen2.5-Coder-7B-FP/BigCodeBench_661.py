import pandas as pd
import seaborn as sns
import numpy as np
def task_func(x, y, labels):
    """
    Create a heatmap using seaborn for given x and y values with labels.

    Parameters:
    x (list): List of x-values.
    y (list): List of y-values.
    labels (list): List of labels for the heatmap.

    Returns:
    ax (Axes): A seaborn heatmap object.
    df (DataFrame): The dataframe used to create the heatmap.
    """
    # Create a DataFrame from the input lists
    df = pd.DataFrame({'x': x, 'y': y, 'value': np.random.rand(len(x))})
    
    # Pivot the DataFrame to create a matrix for the heatmap
    pivot_df = df.pivot('x', 'y', 'value')
    
    # Create the heatmap using seaborn
    ax = sns.heatmap(pivot_df, annot=True, fmt=".2f", cmap="YlGnBu", cbar_kws={'label': 'Value'})
    
    # Set the labels for the heatmap
    ax.set_xlabel('Y Values')
    ax.set_ylabel('X Values')
    ax.set_title('Heatmap of X and Y Values')
    
    return ax, df