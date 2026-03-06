import pandas as pd
import matplotlib.pyplot as plt
from random import sample
COLUMNS = ['A', 'B', 'C', 'D', 'E']
def task_func(df: pd.DataFrame, tuples: list, n_plots: int) -> (pd.DataFrame, list):
    '''
    Remove rows from a dataframe based on column values and generate random scatter plots.

    Parameters:
    - df (pd.DataFrame): The input DataFrame to be modified.
    - tuples (list): A list of tuples, each representing a row's values for removal.
    - n_plots (int): Number of scatter plots to generate from random pairs of columns.

    Returns:
    - pd.DataFrame: The DataFrame after removal of specified rows.
    - list: A list containing matplotlib Axes objects of the generated plots.

    Requirements:
    - pandas
    - matplotlib.pyplot
    - random

    Example:
    >>> df = pd.DataFrame(np.random.randint(0,100,size=(100, 5)), columns=COLUMNS)
    >>> tuples = [(10, 20, 30, 40, 50), (60, 70, 80, 90, 100)]
    >>> modified_df, plots = task_func(df, tuples, 3)
    '''
    # Remove rows from the DataFrame
    for tuple in tuples:
        df = df[~df.isin(tuple).any(axis=1)]

    # Generate random scatter plots
    plots = []
    for _ in range(n_plots):
        x = sample(COLUMNS, 2)
        y = sample(COLUMNS, 2)
        plots.append(plt.scatter(df[x[0]], df[x[1]], c=df[y[0]], cmap='viridis'))
        plt.xlabel(x[0])
        plt.ylabel(x[1])
        plt.colorbar()
        plt.show()

    return df, plots