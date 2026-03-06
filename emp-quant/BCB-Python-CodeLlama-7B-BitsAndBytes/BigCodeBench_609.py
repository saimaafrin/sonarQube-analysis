
from itertools import combinations
from random import sample
import matplotlib.pyplot as plt
import pandas as pd

def task_func(df, tuples, n_plots):
    # Remove rows from the DataFrame based on the list of tuples
    df = df.drop(df.index[tuples])

    # Generate up to 'n_plots' scatter plots for random combinations of two columns from the remaining DataFrame
    plot_list = []
    for i in range(n_plots):
        # Select two random columns from the remaining DataFrame
        cols = sample(df.columns, 2)
        # Create a scatter plot for the two columns
        plot = plt.scatter(df[cols[0]], df[cols[1]])
        # Add the plot to the list of plots
        plot_list.append((cols, plot))

    return df, plot_list

df, plot_list = task_func(df, tuples, n_plots)

# Print the DataFrame after rows have been removed
print(df)

# Print the list of plots
print(plot_list)