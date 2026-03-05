import pandas as pd
import os
import numpy as np
import ast
def task_func(directory):
    """
    Traverse a directory for CSV files, get the file with the longest filename,
    load e-mail data, convert it into a Pandas DataFrame, calculate the sum,
    mean, and median of the list associated with each e-mail, and then draw a
    histogram of the median.

    Parameters
    ----------
    directory : str
        Path to the directory containing the CSV files.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing the data from the CSV file with the longest filename
        augmented with the columns 'sum', 'mean', and 'median'.
    matplotlib.axes._axes.Axes
        Histogram of the median. None if there is no data to plot.
    """
    # Get the list of CSV files in the directory
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]

    # Get the file with the longest filename
    longest_filename = max(csv_files, key=len)

    # Load the data from the CSV file
    df = pd.read_csv(os.path.join(directory, longest_filename))

    # Convert the list column to a list
    df['list'] = df['list'].apply(ast.literal_eval)

    # Calculate the sum, mean, and median of the list associated with each email
    df['sum'] = df['list'].apply(sum)
    df['mean'] = df['list'].apply(np.mean)
    df['median'] = df['list'].apply(np.median)

    # Draw a histogram of the median
    if df['median'].empty:
        return df, None
    else:
        fig, ax = plt.subplots()
        ax.hist(df['median'], bins=50)
        return df, ax
directory = 'path/to/directory'