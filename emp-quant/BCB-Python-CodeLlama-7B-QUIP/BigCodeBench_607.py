
import pandas as pd
import matplotlib.pyplot as plt
from random import sample
# Constants for column names to use in plots
COLUMNS = ['A', 'B', 'C', 'D', 'E']
def task_func(df: pd.DataFrame, tuples: list, n_plots: int) -> (pd.DataFrame, list):
    # Remove rows based on column values
    for col, val in tuples:
        df = df[df[col] != val]
    # Generate random scatter plots
    plots = []
    for i in range(n_plots):
        x = sample(df[COLUMNS[0]], 100)
        y = sample(df[COLUMNS[1]], 100)
        fig, ax = plt.subplots()
        ax.scatter(x, y)
        plots.append(ax)
    return df, plots