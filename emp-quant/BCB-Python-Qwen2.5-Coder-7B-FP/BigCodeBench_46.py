from scipy.stats import zscore
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def task_func(df):
    # Replace missing values with the column's average
    df_filled = df.fillna(df.mean())
    
    # Calculate Z-scores for numeric columns
    z_scores = df_filled.apply(zscore)
    
    # Create a list to hold the Axes objects for histograms
    histograms = []
    
    # Plot histograms for each numeric column
    for column in df_filled.select_dtypes(include=[np.number]).columns:
        ax = df_filled[column].hist(bins=10, alpha=0.75)
        histograms.append(ax)
    
    return z_scores, histograms