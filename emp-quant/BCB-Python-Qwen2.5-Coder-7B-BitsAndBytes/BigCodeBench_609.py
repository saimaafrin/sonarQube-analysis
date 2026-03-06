
import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations
from random import sample

def task_func(df, tuples, n_plots):
    # Remove rows based on the list of tuples
    df_filtered = df[~df.isin(tuples).all(axis=1)]
    
    # Ensure there are enough columns to create plots
    if len(df_filtered.columns) < 2:
        raise ValueError("DataFrame must contain at least two columns to create plots.")
    
    # Select 'n_plots' random pairs of columns for plotting
    plot_pairs = sample(list(combinations(df_filtered.columns, 2)), min(n_plots, len(list(combinations(df_filtered.columns, 2)))))
    
    # Create scatter plots
    plots = []
    for col_pair in plot_pairs:
        fig, ax = plt.subplots()
        ax.scatter(df_filtered[col_pair[0]], df_filtered[col_pair[1]])
        ax.set_xlabel(col_pair[0])
        ax.set_ylabel(col_pair[1])
        ax.set_title(f'Scatter Plot of {col_pair[0]} vs {col_pair[1]}')
        plots.append((col_pair, fig))
    
    return df_filtered, plots