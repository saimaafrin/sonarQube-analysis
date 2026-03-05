import os
import pandas as pd
import re
import matplotlib.pyplot as plt
def task_func(directory: str, pattern: str) -> list:
    """
    Searches a directory for CSV files matching a given regular expression pattern,
    reads sales data from these files, and plots the sales data with month on the x-axis and sales on the y-axis.

    Args:
        directory (str): The directory to search for CSV files.
        pattern (str): The regular expression pattern to match against the file names.

    Returns:
        list: A list of matplotlib.axes._axes.Axes objects, each representing a plot of sales data from a matched CSV file.
    """
    # Create a list to store the plots
    plots = []

    # Iterate over the files in the directory
    for file in os.listdir(directory):
        # Check if the file name matches the pattern
        if re.match(pattern, file):
            # Read the CSV file
            df = pd.read_csv(os.path.join(directory, file))

            # Create a plot of the sales data
            plot = df.plot(x='Month', y='Sales', kind='line')

            # Add the plot to the list
            plots.append(plot)

    # Return the list of plots
    return plots
directory = 'path/to/directory'
pattern = r'^sales_data_\d{4}-\d{2}\.csv$'