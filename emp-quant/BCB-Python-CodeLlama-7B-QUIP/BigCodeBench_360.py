
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def task_func(file_location, sheet_name):
    # Check if the file exists
    if not os.path.exists(file_location):
        raise FileNotFoundError("File not found")

    # Load the Excel file
    df = pd.read_excel(file_location, sheet_name)

    # Calculate the mean and standard deviation of each column
    means = df.mean(axis=0)
    stds = df.std(axis=0)

    # Create a figure object
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111)

    # Plot the bar chart
    ax.bar(means.index, means.values, yerr=stds.values, width=0.5)
    ax.set_xlabel("Columns")
    ax.set_ylabel("Values")
    ax.set_title("Mean and Standard Deviation")

    # Return the figure object
    return fig