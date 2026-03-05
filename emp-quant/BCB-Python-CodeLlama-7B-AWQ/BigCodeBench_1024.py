import numpy as np
import pandas as pd
import seaborn as sns
PLOT_TITLE = "Value Distribution"
def task_func(data_dict):
    # Create a pandas DataFrame from the input dictionary
    df = pd.DataFrame(data_dict)

    # Remove None values
    df = df.dropna()

    # Calculate the minimum and maximum values in the DataFrame
    min_val = df.min().min()
    max_val = df.max().max()

    # Dynamically set the number of bins for the histogram based on the number of data points
    num_bins = min(11, int(df.shape[0] / 2))

    # Create evenly spaced bin edges between the minimum and maximum values
    bin_edges = np.linspace(min_val, max_val, num_bins + 1)

    # Turn off KDE
    sns.set(style="whitegrid")

    # Generate a histogram of the data values using seaborn
    ax = sns.histplot(data=df, x="value", bins=bin_edges, kde=False)

    # Set the plot title
    ax.set_title(PLOT_TITLE)

    # Return the DataFrame and the histogram plot object
    return df, ax
data_dict = {
    "value": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
}