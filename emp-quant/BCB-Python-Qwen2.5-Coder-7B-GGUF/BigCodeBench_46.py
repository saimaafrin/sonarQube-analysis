
from scipy.stats import zscore
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def task_func(df):
    # Replace missing values with the column's average
    df_filled = df.fillna(df.mean())
    
    # Calculate z-scores for numeric columns
    z_scores = df_filled.apply(zscore)
    
    # Plot histograms for each numeric column
    fig, axes = plt.subplots(nrows=len(df_filled.columns), ncols=1, figsize=(8, 4*len(df_filled.columns)))
    for i, column in enumerate(df_filled.columns):
        axes[i].hist(df_filled[column], bins=10, edgecolor='black')
        axes[i].set_title(f'Histogram of {column}')
        axes[i].set_xlabel(column)
        axes[i].set_ylabel('Frequency')
    
    # Adjust layout and show plot
    plt.tight_layout()
    plt.show()
    
    return z_scores, axes