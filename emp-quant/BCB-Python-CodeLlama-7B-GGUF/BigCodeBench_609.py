
from itertools import combinations
from random import sample
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, tuples, n_plots):
    # Remove rows from the DataFrame based on the list of tuples
    for tuple in tuples:
        df = df[~(df[tuple[0]] == tuple[1])]

    # Generate up to 'n_plots' scatter plots for random combinations of two columns from the remaining DataFrame
    plots = []
    for i in range(n_plots):
        # Select two random columns from the remaining DataFrame
        columns = sample(df.columns, 2)

        # Create a scatter plot for the two columns
        fig, ax = plt.subplots()
        ax.scatter(df[columns[0]], df[columns[1]])
        ax.set_xlabel(columns[0])
        ax.set_ylabel(columns[1])
        ax.set_title(f"Scatter Plot for {columns[0]} and {columns[1]}")
        plots.append((columns[0], columns[1], fig))

    return df, plots