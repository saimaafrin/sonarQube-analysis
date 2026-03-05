
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
    
    # Create a box plot for each column
    fig, ax = plt.subplots(figsize=(15, 10))
    df.boxplot(ax=ax)
    ax.set_title('Box Plot of Normalized Numeric Columns')
    ax.set_xlabel('Columns')
    ax.set_ylabel('Values')
    
    return df, ax