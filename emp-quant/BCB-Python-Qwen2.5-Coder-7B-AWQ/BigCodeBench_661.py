import pandas as pd
import seaborn as sns
import numpy as np
def task_func(x, y, labels):
    """
    Create a heatmap using the seaborn library for "x" as x-values and "y" as y-values with labels.
    
    Parameters:
    x (list): A list of x-values.
    y (list): A list of y-values.
    labels (list): A list of labels for the x and y values.
    
    Returns:
    ax (Axes): A seaborn heatmap object.
    df (DataFrame): The dataframe used to create the heatmap.
    """
    # Create a DataFrame from the input data
    df = pd.DataFrame(np.random.rand(len(x), len(y)), index=labels, columns=labels)
    
    # Create a heatmap using seaborn
    ax = sns.heatmap(df, annot=True, fmt=".2f", cmap='YlGnBu')
    
    return ax, df