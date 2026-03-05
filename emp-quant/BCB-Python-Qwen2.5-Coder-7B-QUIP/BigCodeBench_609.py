
from itertools import combinations
from random import sample
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, tuples, n_plots):
    # Remove rows based on the list of tuples
    df = df[~df.isin(tuples).all(axis=1)]
    
    # Generate random combinations of two columns for scatter plots
    columns = df.columns.tolist()
    plot_combinations = list(combinations(columns, 2))
    selected_combinations = sample(plot_combinations, n_plots)
    
    # Create scatter plots for the selected combinations
    plot_objects = []
    for col1, col2 in selected_combinations:
        plt.figure()
        plt.scatter(df[col1], df[col2])
        plt.xlabel(col1)
        plt.ylabel(col2)
        plot_objects.append(plt)

    return df, selected_combinations, plot_objects