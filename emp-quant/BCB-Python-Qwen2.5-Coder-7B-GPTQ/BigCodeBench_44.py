from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def task_func(df):
    # Replace missing values with the mean of the column
    df.fillna(df.mean(), inplace=True)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Normalize the numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    
    # Create a figure and a set of subplots
    fig, axes = plt.subplots(nrows=1, ncols=len(numeric_cols), figsize=(15, 5))
    
    # Plot a box plot for each numeric column
    for i, col in enumerate(numeric_cols):
        df[col].plot(kind='box', ax=axes[i])
        axes[i].set_title(col)
    
    # Adjust layout to prevent overlap
    plt.tight_layout()
    
    return df, axes