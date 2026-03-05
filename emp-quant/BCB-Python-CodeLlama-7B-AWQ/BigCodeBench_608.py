import seaborn as sns
from random import sample
import pandas as pd
import numpy as np
COLUMNS = ['A', 'B', 'C', 'D', 'E']
def task_func(df, tuples, n_plots):
    # Remove rows from a dataframe based on values of multiple columns
    for col, val in tuples:
        df = df[df[col] != val]
    # Create n random pairs of two columns against each other to generate pairplots
    pairs = sample(COLUMNS, n_plots)
    axs = []
    for i in range(n_plots):
        ax = sns.pairplot(df, x_vars=pairs[i], y_vars=pairs[(i+1)%n_plots])
        axs.append(ax)
    return df, axs
df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                   'B': [1, 2, 3, 4, 5],
                   'C': [1, 2, 3, 4, 5],
                   'D': [1, 2, 3, 4, 5],
                   'E': [1, 2, 3, 4, 5]})
tuples = [('A', 1), ('B', 2)]