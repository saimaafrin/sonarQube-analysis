import seaborn as sns
from random import sample
COLUMNS = ['A', 'B', 'C', 'D', 'E']
def task_func(df, tuples, n_plots):
    """
    Remove rows from a dataframe based on values of multiple columns, and then create n random pairs of two columns 
    against each other to generate pairplots.

    Parameters:
    df (DataFrame): The pandas DataFrame.
    tuples (list of tuple): A list of tuples, where each tuple represents a row to be removed based on its values.
    n_plots (int): The number of pairplots to be generated using randomly selected column pairs.

    Returns:
    tuple: A tuple containing:
        - DataFrame: The modified DataFrame after removing specified rows.
        - list of Axes: A list containing the generated pairplots.

    Requirements:
    - seaborn
    - random

    Example:
    >>> import numpy as np, pandas as pd
    >>> df = pd.DataFrame(np.random.randint(0,100,size=(100, 5)), columns=list('ABCDE'))
    >>> tuples = [(10, 20, 30, 40, 50), (60, 70, 80, 90, 100)]
    >>> modified_df, plots = task_func(df, tuples, 3)
    """
    # Remove rows from dataframe
    for tuple in tuples:
        df = df[~df.isin(tuple).any(1)]

    # Generate random pairs of columns
    pairs = sample(list(zip(COLUMNS, COLUMNS)), n_plots)

    # Generate pairplots
    fig, axes = plt.subplots(n_plots, 1, figsize=(10, 10))
    for i, pair in enumerate(pairs):
        sns.pairplot(df, hue='A', vars=pair, diag_kind='kde', plot_kws={'alpha': 0.5}, height=4, aspect=1.5)
        axes[i].set_title(f'{pair[0]} vs {pair[1]}')

    return df, axes