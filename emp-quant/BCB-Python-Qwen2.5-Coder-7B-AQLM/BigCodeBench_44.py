
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def task_func(df):
    # Replace missing values with the column's average
    df.fillna(df.mean(), inplace=True)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Normalize the numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    
    # Create a box plot for each column
    fig, axes = plt.subplots(nrows=1, ncols=len(numeric_cols), figsize=(15, 5))
    
    for i, col in enumerate(numeric_cols):
        axes[i].boxplot(df[col])
        axes[i].set_title(col)
    
    plt.tight_layout()
    plt.show()
    
    return df, axes