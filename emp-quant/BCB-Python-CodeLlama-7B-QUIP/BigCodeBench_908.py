
import os
import pandas as pd
import re
import matplotlib.pyplot as plt

def task_func(directory: str, pattern: str) -> list:
    # Create a list to store the matplotlib axes objects
    axes_list = []

    # Loop through the directory and find all files matching the pattern
    for file in os.listdir(directory):
        if re.match(pattern, file):
            # Read the file and extract the sales data
            df = pd.read_csv(os.path.join(directory, file))
            sales = df['Sales']

            # Create a plot of the sales data
            fig, ax = plt.subplots()
            ax.plot(sales)
            axes_list.append(ax)

    return axes_list