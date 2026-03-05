
import pandas as pd
import seaborn as sns
import numpy as np
# Constants
LABELS = ['H\u2082O', 'O\u2082', 'CO\u2082', 'N\u2082', 'Ar']
def task_func(x, y, labels):
    # Create a dataframe with the x and y values
    df = pd.DataFrame({'x': x, 'y': y, 'labels': labels})
    # Create a seaborn heatmap
    ax = sns.heatmap(df, annot=True, cmap='coolwarm')
    return ax, df