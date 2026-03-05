import pandas as pd
import seaborn as sns
import numpy as np
def task_func(x, y, labels):
    """
    Create a heatmap using the seaborn library for "x" as x-values and "y" as y-values with labels.
    The function should output with:
        ax (Axes): A seaborn heatmap object.
        df (DataFrame): The dataframe used to create the heatmap.
    """
    # Create a dataframe with the x and y values and the corresponding labels
    df = pd.DataFrame({'x': x, 'y': y, 'label': labels})

    # Create a seaborn heatmap with the dataframe
    ax = sns.heatmap(df, annot=True, cmap='viridis')

    # Set the x and y labels
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # Return the heatmap and the dataframe
    return ax, df
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
labels = ['H\u2082O', 'O\u2082', 'CO\u2082', 'N\u2082', 'Ar']