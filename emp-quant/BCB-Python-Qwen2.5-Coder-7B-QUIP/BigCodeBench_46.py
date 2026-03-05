
from scipy.stats import zscore
import matplotlib.pyplot as plt
import pandas as pd

def task_func(df):
    # Replace missing values with the column's average
    df = df.fillna(df.mean())
    
    # Calculate z-scores for numeric columns
    z_scores = df.apply(zscore)
    
    # Create a list to hold the histogram axes
    histograms = []
    
    # Plot histograms for each numeric column
    for column in df.columns:
        if df[column].dtype in ['int64', 'float64']:
            ax = plt.subplot(1, 1, 1)
            df[column].hist(ax=ax, bins=10)
            histograms.append(ax)
    
    # Return the DataFrame with z-scores and the list of histogram axes
    return z_scores, histograms