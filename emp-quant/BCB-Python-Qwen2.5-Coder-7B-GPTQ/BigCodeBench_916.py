import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def task_func(df: pd.DataFrame) -> tuple:
    """
    Visualize the distribution of stock closing prices using both a box plot and a histogram within a single figure.
    
    Parameters:
    - df: A pandas DataFrame containing stock data with a 'Close' column representing the closing prices.
    
    Returns:
    - A tuple containing two matplotlib.axes._axes.Axes objects: the first for the boxplot and the second for the histogram.
    """
    # Create a figure and a set of subplots
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Plot the box plot
    sns.boxplot(x=df['Close'], ax=axes[0])
    axes[0].set_title('Box Plot of Closing Prices')
    
    # Plot the histogram
    sns.histplot(df['Close'], kde=True, ax=axes[1])
    axes[1].set_title('Histogram of Closing Prices')
    
    # Adjust layout to prevent overlap
    plt.tight_layout()
    
    return axes