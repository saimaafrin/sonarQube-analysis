
from scipy.stats import zscore
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def task_func(df):
    # Replace missing values with the column's average
    df.fillna(df.mean(), inplace=True)
    
    # Calculate Z-scores for numeric columns
    z_scores = df.select_dtypes(include=[np.number]).apply(zscore)
    
    # Plot histograms for each numeric column
    fig, axes = plt.subplots(nrows=z_scores.shape[1], ncols=1, figsize=(8, 6 * z_scores.shape[1]))
    axes = axes.flatten() if z_scores.shape[1] > 1 else [axes]
    
    for ax, column in zip(axes, z_scores.columns):
        ax.hist(z_scores[column], bins=10, edgecolor='black')
        ax.set_title(f'Histogram of {column} Z-scores')
        ax.set_xlabel('Z-scores')
        ax.set_ylabel('Frequency')
    
    plt.tight_layout()
    plt.show()
    
    return z_scores, axes