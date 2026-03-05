from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def task_func(df):
    """
    Normalize numeric columns in a DataFrame and draw a box plot for each column.
    Missing values are replaced by column's average.
    
    Parameters:
    df (pd.DataFrame): Input DataFrame with numeric columns.
    
    Returns:
    pd.DataFrame: A pandas DataFrame after normalization.
    Axes: A matplotlib Axes displaying a box plot for each column.
    """
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Replace missing values with the mean of the column
    df.fillna(df.mean(), inplace=True)
    
    # Normalize the numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    
    # Create a box plot for each column
    fig, ax = plt.subplots()
    df.boxplot(ax=ax)
    ax.set_title('Box Plot of Normalized Numeric Columns')
    
    return df, ax