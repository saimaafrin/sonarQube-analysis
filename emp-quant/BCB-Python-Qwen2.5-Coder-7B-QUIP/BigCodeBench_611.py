
from random import sample
import matplotlib.pyplot as plt
import pandas as pd

# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def task_func(df, tuples, n_plots):
    # Remove rows based on the condition
    df = df[~df['A'].isin(tuples[0]) & ~df['B'].isin(tuples[1]) & ~df['C'].isin(tuples[2]) & ~df['D'].isin(tuples[3]) & ~df['E'].isin(tuples[4])]

    # Generate n random line plots
    plot_details = []
    for _ in range(n_plots):
        # Randomly select two columns to plot
        cols = sample(COLUMNS, 2)
        # Create a line plot
        plt.figure()
        plt.plot(df[cols[0]], df[cols[1]], 'o')
        plt.xlabel(cols[0])
        plt.ylabel(cols[1])
        plt.title(f'Plot of {cols[0]} vs {cols[1]}')
        # Store the plot details
        plot_details.append((cols[0], cols[1]))

    return df, plot_details