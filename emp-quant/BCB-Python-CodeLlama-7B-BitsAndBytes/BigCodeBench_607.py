
import pandas as pd
import matplotlib.pyplot as plt
from random import sample

# Constants for column names to use in plots
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def task_func(df: pd.DataFrame, tuples: list, n_plots: int) -> (pd.DataFrame, list):
    # Remove rows from the DataFrame based on the specified tuples
    for col, val in tuples:
        df = df[df[col] != val]

    # Generate random scatter plots
    plots = []
    for i in range(n_plots):
        x = sample(df[COLUMNS[0]], 100)
        y = sample(df[COLUMNS[1]], 100)
        ax = plt.scatter(x, y)
        plots.append(ax)

    return df, plots

df, plots = task_func(df, tuples, n_plots)

print(df)
print(plots)