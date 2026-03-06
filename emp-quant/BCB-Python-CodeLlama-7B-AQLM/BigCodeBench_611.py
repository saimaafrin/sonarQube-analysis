from random import sample
import matplotlib.pyplot as plt
COLUMNS = ['A', 'B', 'C', 'D', 'E']
def task_func(df, tuples, n_plots):
    """
    Removes rows from a DataFrame based on values of multiple columns, 
    and then create n random line plots of two columns against each other.

    Parameters:
    - df (pd.DataFrame): The input pandas DataFrame.
    - tuples (list of tuple): A list of tuples, each tuple represents values in a row to be removed.
    - n_plots (int): The number of line plots to generate.

    Returns:
    - (pd.DataFrame, list): A tuple containing the modified DataFrame and a list of plot details.
      Each entry in the plot details list is a tuple containing the two columns plotted against each other.

    Requirements:
    - matplotlib.pyplot
    - random

    Example:
    >>> import numpy as np, pandas as pd
    >>> df = pd.DataFrame(np.random.randint(0,100,size=(100, 5)), columns=list('ABCDE'))
    >>> tuples = [(10, 20, 30, 40, 50), (60, 70, 80, 90, 100)]
    >>> modified_df, plot_details = task_func(df, tuples, 3)
    """
    # Remove rows from the DataFrame
    for tuple_ in tuples:
        df = df[~df.isin(tuple_).any(axis=1)]

    # Create n random line plots of two columns against each other
    plot_details = []
    for _ in range(n_plots):
        # Select two random columns
        col1 = sample(COLUMNS, 1)[0]
        col2 = sample(COLUMNS, 1)[0]
        while col1 == col2:
            col2 = sample(COLUMNS, 1)[0]

        # Create a line plot of the two columns
        plt.plot(df[col1], df[col2])
        plt.xlabel(col1)
        plt.ylabel(col2)
        plt.title(f'{col1} vs {col2}')
        plt.show()

        # Add the two columns to the plot details list
        plot_details.append((col1, col2))

    return df, plot_details