
from itertools import combinations
from random import sample
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, tuples, n_plots):
    # Remove rows based on the list of tuples
    df = df[~df.isin(tuples).all(axis=1)]
    
    # Generate up to 'n_plots' scatter plots for random combinations of two columns
    plots = []
    for _ in range(n_plots):
        if len(df.columns) < 2:
            break
        cols = sample(df.columns, 2)
        plot = df.plot.scatter(x=cols[0], y=cols[1])
        plots.append((cols, plot))
    
    return df, plots