
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def task_func(df):
    # Replace NaN values with the average of the column
    df.fillna(df.mean(), inplace=True)
    
    # Calculate statistics for each numeric column
    stats = df.describe()
    
    # Create a list to hold the distribution plots
    plots = []
    
    # Create a figure with subplots for each numeric column
    fig, axes = plt.subplots(nrows=len(df.select_dtypes(include=[np.number]).columns), ncols=1, figsize=(8, 6*len(df.select_dtypes(include=[np.number]).columns)))
    
    # Iterate over each numeric column and create a distribution plot
    for i, column in enumerate(df.select_dtypes(include=[np.number]).columns):
        sns.histplot(df[column], bins=10, kde=True, ax=axes[i])
        axes[i].set_title(f'Distribution of {column}')
        axes[i].set_xlabel(column)
        axes[i].set_ylabel('Frequency')
        plots.append(axes[i])
    
    # Adjust layout and return the results
    plt.tight_layout()
    return stats, plots