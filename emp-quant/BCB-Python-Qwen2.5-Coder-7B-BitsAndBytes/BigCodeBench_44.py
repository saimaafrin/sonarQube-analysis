
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def task_func(df):
    # Replace missing values with the mean of the respective column
    df.fillna(df.mean(), inplace=True)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Normalize the numeric columns
    df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    
    # Create a figure to hold all the box plots
    fig, axes = plt.subplots(len(df.columns), 1, figsize=(8, len(df.columns)*2))
    
    # Plot a box plot for each column
    for i, col in enumerate(df.columns):
        axes[i].boxplot(df[col])
        axes[i].set_title(f'Box Plot of {col}')
    
    # Adjust layout to prevent overlap
    plt.tight_layout()
    
    return df_scaled, axes