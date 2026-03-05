
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(df: pd.DataFrame) -> tuple:
    """
    Visualize the distribution of stock closing prices using both a box plot and a histogram within a single figure.
    
    Parameters:
    df (pd.DataFrame): DataFrame containing stock data with a 'Close' column.
    
    Returns:
    tuple: A tuple containing two matplotlib.axes._axes.Axes objects: the first for the boxplot and the second for the histogram.
    """
    # Create a figure with two subplots
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    # Box plot of closing prices
    sns.boxplot(x=df['Close'], ax=axes[0])
    axes[0].set_title('Box Plot of Closing Prices')
    
    # Histogram of closing prices
    sns.histplot(df['Close'], ax=axes[1], kde=True)
    axes[1].set_title('Histogram of Closing Prices')
    
    # Adjust layout
    plt.tight_layout()
    
    return axes