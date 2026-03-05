
import pandas as pd
import matplotlib.pyplot as plt
from itertools import cycle

def task_func(df, groups=['A', 'B', 'C', 'D', 'E']):
    # Check if df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input 'df' must be a pandas DataFrame.")
    
    # Check if required columns exist
    required_columns = ['Date', 'Value']
    if not all(column in df for column in required_columns):
        raise ValueError("Input DataFrame 'df' must contain 'Date' and 'Value' columns.")
    
    # Create a color cycle for plotting
    colors = cycle('bgrcmyk')
    
    # Create a new figure
    fig, ax = plt.subplots()
    
    # Plot each group
    for group in groups:
        if group in df['Date'].unique():
            ax.scatter(df[df['Date'] == group]['Date'], df[df['Date'] == group]['Value'], color=next(colors), label=group)
    
    # Set plot properties
    ax.set_title('Scatterplot of Values for Each Group Over Time')
    ax.set_xlabel('Date (ordinal)')
    ax.set_ylabel('Value')
    
    # Show legend
    ax.legend()
    
    # Return the Axes object
    return ax