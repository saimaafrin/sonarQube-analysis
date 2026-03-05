
from itertools import combinations
from random import sample
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, tuples, n_plots):
    # Remove rows from the DataFrame based on the tuples
    for tuple in tuples:
        df = df.drop(df.loc[tuple[0] == tuple[1]].index)

    # Generate random combinations of columns for the plots
    columns = sample(df.columns, n_plots)

    # Create a list of tuples containing the column names and the corresponding plot objects
    plots = [(columns[i], columns[i+1]) for i in range(n_plots)]

    # Return the DataFrame and the list of tuples
    return df, plots