import pandas as pd
import seaborn as sns
import numpy as np
LABELS = ['H\u2082O', 'O\u2082', 'CO\u2082', 'N\u2082', 'Ar']
def task_func(x, y, labels):
    """
    Create a heatmap using the seaborn library for "x" as x-values and "y" as y-values with labels.
    The function should output with:
        ax (Axes): A seaborn heatmap object.
        df (DataFrame): The dataframe used to create the heatmap.
    """
    # Create a dataframe with the given x and y values
    df = pd.DataFrame({'x': x, 'y': y})

    # Create a seaborn heatmap with the given labels
    ax = sns.heatmap(df, annot=True, cmap='coolwarm', cbar=False, xticklabels=LABELS, yticklabels=LABELS)

    return ax, df
x = np.arange(1, 6)
y = np.arange(1, 6)
labels = LABELS