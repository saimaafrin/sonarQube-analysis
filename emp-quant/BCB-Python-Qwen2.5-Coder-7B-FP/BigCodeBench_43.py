import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
def task_func(df):
    # Replace NaN values with the average of the column
    df_filled = df.fillna(df.mean())
    
    # Calculate statistics for each numeric column
    stats = df_filled.describe()
    
    # Create a list to hold the distribution plots
    plots = []
    
    # Create a figure to hold all plots
    fig, axes = plt.subplots(nrows=len(df_filled.select_dtypes(include=[np.number]).columns), ncols=1, figsize=(8, 6*len(df_filled.select_dtypes(include=[np.number]).columns)))
    
    # Iterate over each numeric column and create a distribution plot
    for i, column in enumerate(df_filled.select_dtypes(include=[np.number]).columns):
        plot = sns.histplot(df_filled[column], bins=10, ax=axes[i])
        plot.set_title(f'Distribution of {column}')
        plots.append(plot)
    
    # Adjust layout and return the results
    plt.tight_layout()
    return stats, plots