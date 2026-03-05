
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def task_func(df):
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Replace missing values with the column's average
    df = df.fillna(df.mean())
    
    # Normalize the numeric columns
    numeric_columns = df.select_dtypes(include=['number'])
    df[numeric_columns.columns] = scaler.fit_transform(numeric_columns)
    
    # Create a box plot for each column
    fig, axes = plt.subplots(nrows=1, ncols=len(numeric_columns.columns), figsize=(15, 5))
    
    for i, column in enumerate(numeric_columns.columns):
        axes[i].boxplot(df[column], vert=False)
        axes[i].set_title(column)
    
    plt.tight_layout()
    
    return df, axes