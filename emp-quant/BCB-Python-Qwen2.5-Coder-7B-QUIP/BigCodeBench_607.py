
import pandas as pd
import matplotlib.pyplot as plt
from random import sample
# Constants for column names to use in plots
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def task_func(df: pd.DataFrame, tuples: list, n_plots: int) -> (pd.DataFrame, list):
    # Remove rows based on the tuples
    df = df[~df.apply(lambda row: any(row[col] == tuple_val for col, tuple_val in zip(COLUMNS, tuple)), axis=1)]
    
    # Generate random scatter plots
    fig, axes = plt.subplots(nrows=n_plots, ncols=1, figsize=(10, n_plots*5))
    if n_plots == 1:
        axes = [axes]
    
    for ax in axes:
        ax.scatter(df['A'], df['B'], c='blue')
        ax.set_xlabel('A')
        ax.set_ylabel('B')
        ax.set_title('Scatter Plot')
    
    return df, axes