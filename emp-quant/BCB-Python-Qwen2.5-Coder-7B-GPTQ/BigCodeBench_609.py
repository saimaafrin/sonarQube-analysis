from itertools import combinations
from random import sample
import pandas as pd
import matplotlib.pyplot as plt
def task_func(df, tuples, n_plots):
    # Remove rows based on the list of tuples
    df_filtered = df[~df.isin(tuples).all(axis=1)]
    
    # Generate up to 'n_plots' scatter plots for random combinations of two columns
    plots = []
    for _ in range(n_plots):
        if len(df_filtered.columns) < 2:
            break
        cols = sample(list(df_filtered.columns), 2)
        fig, ax = plt.subplots()
        df_filtered.plot.scatter(x=cols[0], y=cols[1], ax=ax)
        plots.append((cols, fig))
    
    return df_filtered, plots
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [2, 3, 4, 5, 6]
})
n_plots = 2