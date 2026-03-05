
import numpy as np
import pandas as pd
import seaborn as sns
# Constants
PLOT_TITLE = "Value Distribution"

def task_func(data_dict):
    # Create a DataFrame from the dictionary, excluding None values
    df = pd.DataFrame(list(data_dict.values()))
    
    # Remove None values
    df = df[~df.isnull().any(axis=1)]
    
    # Check if the DataFrame is empty
    if df.empty:
        return df, None
    
    # Calculate the number of bins for the histogram
    num_points = df.shape[0]
    num_bins = min(11, max(2, num_points // 2))
    
    # Calculate the minimum and maximum values
    min_value = df.min().min()
    max_value = df.max().max()
    
    # Create evenly spaced bin edges
    bin_edges = np.linspace(min_value, max_value, num_bins + 1)
    
    # Create the histogram plot
    plot = sns.histplot(df, kde=False, bins=bin_edges, color='blue')
    
    # Set the plot title
    plot.set_title(PLOT_TITLE)
    
    # Return the DataFrame and the plot
    return df, plot