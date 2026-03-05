import pandas as pd
import matplotlib.pyplot as plt
def task_func(df, bins=20):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")
    
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("DataFrame is empty")
    
    # Get the last column of the DataFrame
    last_column = df.columns[-1]
    
    # Create a histogram of the last column
    ax = df[last_column].hist(bins=bins)
    
    # Set the title of the histogram
    ax.set_title(f'Histogram of {last_column}')
    
    # Set the labels for the x-axis and y-axis
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    
    # Return the Axes object
    return ax