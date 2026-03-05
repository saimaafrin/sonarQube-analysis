
import numpy as np
import pandas as pd
import seaborn as sns
# Constants
PLOT_TITLE = "Value Distribution"
def task_func(data_dict):
    # Create a pandas DataFrame from the input dictionary
    df = pd.DataFrame(data_dict)
    # Remove None values
    df = df.dropna()
    # Calculate the minimum and maximum values in the DataFrame
    min_val = df.min().min()
    max_val = df.max().max()
    # Calculate the number of bins for the histogram
    num_bins = min(11, int(df.shape[0]/2))
    # Create evenly spaced bin edges between the minimum and maximum values
    bin_edges = np.linspace(min_val, max_val, num_bins+1)
    # Create a seaborn histogram plot object
    sns_plot = sns.histplot(data=df, bins=bin_edges, kde=False, title=PLOT_TITLE)
    # Return the DataFrame and the seaborn histogram plot object
    return df, sns_plot