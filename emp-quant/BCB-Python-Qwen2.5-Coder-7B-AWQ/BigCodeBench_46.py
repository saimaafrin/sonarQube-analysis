from scipy.stats import zscore
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def task_func(df):
    # Replace missing values with the column's average
    df.fillna(df.mean(), inplace=True)
    
    # Calculate Z-scores for numeric columns
    z_scores = df.apply(zscore)
    
    # Create a list to hold the Axes objects for histograms
    histograms = []
    
    # Plot histograms for each numeric column
    for column in df.select_dtypes(include=[np.number]).columns:
        ax = df[column].hist(bins=10, alpha=0.7, color='blue')
        histograms.append(ax)
    
    return z_scores, histograms