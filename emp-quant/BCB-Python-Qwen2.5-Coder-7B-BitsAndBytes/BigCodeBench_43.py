
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def task_func(df):
    # Replace NaN values with the average of the column
    df = df.fillna(df.mean())
    
    # Calculate statistics for each numeric column
    stats_df = df.describe()
    
    # Create a list to hold the distribution plots
    axes_list = []
    
    # Plot distribution charts for each numeric column
    fig, axes = plt.subplots(nrows=len(df.select_dtypes(include=[np.number]).columns), ncols=1, figsize=(8, len(df.select_dtypes(include=[np.number]).columns)*4))
    if len(df.select_dtypes(include=[np.number]).columns) == 1:
        ax = axes
        axes_list.append(ax)
        sns.histplot(df.select_dtypes(include=[np.number]).iloc[:, 0], kde=True, bins=10, ax=ax)
    else:
        for i, col in enumerate(df.select_dtypes(include=[np.number]).columns):
            ax = axes[i]
            axes_list.append(ax)
            sns.histplot(df[col], kde=True, bins=10, ax=ax)
    
    plt.tight_layout()
    plt.show()
    
    return stats_df, axes_list