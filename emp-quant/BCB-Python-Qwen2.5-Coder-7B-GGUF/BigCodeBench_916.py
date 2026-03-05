
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(df: pd.DataFrame) -> tuple:
    # Create a figure with a 1x2 grid of subplots
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    # Plot the box plot on the first subplot
    sns.boxplot(x=df['closing_price'], ax=axes[0])
    axes[0].set_title('Box Plot of Closing Prices')
    
    # Plot the histogram on the second subplot
    sns.histplot(df['closing_price'], kde=True, ax=axes[1])
    axes[1].set_title('Histogram of Closing Prices')
    
    # Adjust layout to prevent overlap
    plt.tight_layout()
    
    # Return the axes objects
    return axes