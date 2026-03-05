
from itertools import combinations
from random import sample
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, tuples, n_plots):
    # Remove rows based on the list of tuples
    df = df[~df.isin(tuples).all(axis=1)]
    
    # Generate up to 'n_plots' scatter plots for random combinations of two columns
    plot_list = []
    for _ in range(min(n_plots, len(list(combinations(df.columns, 2))))):
        cols = sample(list(combinations(df.columns, 2)), 1)[0]
        fig, ax = plt.subplots()
        df.plot.scatter(x=cols[0], y=cols[1], ax=ax)
        plot_list.append((cols, fig))
    
    return df, plot_list