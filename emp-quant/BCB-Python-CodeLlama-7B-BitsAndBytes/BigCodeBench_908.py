
import os
import pandas as pd
import re
import matplotlib.pyplot as plt

def task_func(directory: str, pattern: str) -> list:
    # Create a list to store the matplotlib.axes._axes.Axes objects
    plots = []

    # Loop through all files in the directory
    for file in os.listdir(directory):
        # Check if the file matches the regular expression pattern
        if re.search(pattern, file):
            # Read the CSV file using pandas
            df = pd.read_csv(os.path.join(directory, file))

            # Create a plot of the sales data
            plot = df.plot(kind='line', x='Month', y='Sales')

            # Add the plot to the list of plots
            plots.append(plot)

    # Return the list of plots
    return plots

# Show the plots
for plot in plots:
    plt.show()