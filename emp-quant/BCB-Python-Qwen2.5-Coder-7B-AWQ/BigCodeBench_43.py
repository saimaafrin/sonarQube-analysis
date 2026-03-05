import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
def task_func(df):
    # Replace NaN values with the average of the column
    df = df.fillna(df.mean())
    
    # Calculate statistics for each numeric column
    stats = df.describe()
    
    # Create a list to hold the distribution plots
    plots = []
    
    # Create a figure to hold all plots
    fig, axes = plt.subplots(nrows=len(df.select_dtypes(include=[np.number]).columns), ncols=1, figsize=(8, 6*len(df.select_dtypes(include=[np.number]).columns)))
    
    # Iterate over each numeric column and create a distribution plot
    for i, column in enumerate(df.select_dtypes(include=[np.number]).columns):
        plot = sns.histplot(df[column], bins=10, ax=axes[i])
        plots.append(plot)
    
    # Adjust layout and return the results
    plt.tight_layout()
    return (stats, plots)