import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random import sample
COLUMNS = ['A', 'B', 'C', 'D', 'E']
def task_func(df, tuples, n_plots):
    """
    Removes rows from a DataFrame based on values of multiple columns, and then creates n random line plots of two columns against each other.
    The function should output with:
        (pd.DataFrame, list): A tuple containing the modified DataFrame and a list of plot details.
        Each entry in the plot details list is a tuple containing the two columns plotted against each other.
    """
    # Remove rows based on values of multiple columns
    for col, val in tuples:
        df = df[df[col] != val]

    # Create n random line plots of two columns against each other
    plot_details = []
    for _ in range(n_plots):
        col1 = sample(COLUMNS, 1)[0]
        col2 = sample(COLUMNS, 1)[0]
        while col1 == col2:
            col2 = sample(COLUMNS, 1)[0]
        plot_details.append((col1, col2))
        plt.plot(df[col1], df[col2])
        plt.xlabel(col1)
        plt.ylabel(col2)
        plt.title(f"{col1} vs {col2}")
        plt.show()

    return df, plot_details
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [2, 4, 6, 8, 10],
    'C': [3, 6, 9, 12, 15],
    'D': [4, 8, 12, 16, 20],
    'E': [5, 10, 15, 20, 25]
})
tuples = [('A', 3), ('B', 6)]
n_plots = 2