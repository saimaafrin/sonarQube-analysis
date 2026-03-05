import seaborn as sns
from random import sample
import pandas as pd
import matplotlib.pyplot as plt
COLUMNS = ['A', 'B', 'C', 'D', 'E']
def task_func(df, tuples, n_plots):
    """
    Removes rows from a dataframe based on values of multiple columns, and then creates n random pairs of two columns against each other to generate pairplots.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame.
    tuples (list of tuples): A list of tuples where each tuple contains the column names to be used for filtering.
    n_plots (int): The number of pairplots to generate.
    
    Returns:
    tuple: A tuple containing:
        DataFrame: The modified DataFrame after removing specified rows.
        list of Axes: A list containing the generated pairplots.
    """
    # Remove rows based on the specified tuples
    for col1, col2 in tuples:
        df = df[(df[col1] != df[col2])]
    
    # Generate n random pairs of columns and create pairplots
    pairplot_list = []
    for _ in range(n_plots):
        col1, col2 = sample(COLUMNS, 2)
        pairplot = sns.pairplot(df[[col1, col2]])
        pairplot_list.append(pairplot)
    
    return df, pairplot_list