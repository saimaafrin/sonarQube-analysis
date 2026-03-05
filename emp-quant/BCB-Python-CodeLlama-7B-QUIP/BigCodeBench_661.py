
import pandas as pd
import seaborn as sns
import numpy as np
# Constants
LABELS = ['H\u2082O', 'O\u2082', 'CO\u2082', 'N\u2082', 'Ar']
def task_func(x, y, labels):
    # Create a dataframe with the x and y values
    df = pd.DataFrame({'x': x, 'y': y, 'labels': labels})
    # Create a seaborn heatmap object
    ax = sns.heatmap(df, cmap='viridis')
    # Set the x and y labels
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    # Set the labels for the heatmap
    ax.set_xticks(np.arange(0, 10, 1))
    ax.set_yticks(np.arange(0, 10, 1))
    ax.set_xticklabels(LABELS)
    ax.set_yticklabels(LABELS)
    return ax