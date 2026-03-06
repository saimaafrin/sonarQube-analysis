
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df: pd.DataFrame) -> tuple:
    # Create a figure with 1 row and 2 columns
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Box plot of closing prices
    box_plot = df['Close'].boxplot(ax=axes[0])
    axes[0].set_title('Box Plot of Closing Prices')
    
    # Histogram of closing prices
    hist_plot = df['Close'].hist(ax=axes[1], bins=30)
    axes[1].set_title('Histogram of Closing Prices')
    
    # Adjust layout to prevent overlap
    plt.tight_layout()
    
    return (axes[0], axes[1])