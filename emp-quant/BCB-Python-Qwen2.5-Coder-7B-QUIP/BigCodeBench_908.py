
import os
import pandas as pd
import re
import matplotlib.pyplot as plt

def task_func(directory: str, pattern: str) -> list:
    # Initialize an empty list to store the plot objects
    plots = []

    # Search for CSV files matching the given pattern
    for filename in os.listdir(directory):
        if re.match(pattern, filename):
            # Read the CSV file into a pandas DataFrame
            df = pd.read_csv(os.path.join(directory, filename))

            # Plot the sales data
            fig, ax = plt.subplots()
            ax.plot(df['Month'], df['Sales'], marker='o')
            ax.set_xlabel('Month')
            ax.set_ylabel('Sales')
            ax.set_title(f'Sales Data from {filename}')

            # Append the plot object to the list
            plots.append(ax)

    return plots