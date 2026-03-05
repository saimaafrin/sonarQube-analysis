
import seaborn as sns
from random import sample
import pandas as pd
import matplotlib.pyplot as plt

# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def task_func(df, tuples, n_plots):
    """
    Removes rows from a dataframe based on values of multiple columns, and then creates n random pairs of two columns against each other to generate pairplots.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame.
    tuples (list of tuples): A list of tuples where each tuple contains column names and values to remove.
    n_plots (int): The number of random pairs of columns to generate pairplots for.
    
    Returns:
    tuple: A tuple containing:
        DataFrame: The modified DataFrame after removing specified rows.
        list of Axes: A list containing the generated pairplots.
    """
    # Remove rows based on specified tuples
    for col1, col2, value1, value2 in tuples:
        df = df[(df[col1] != value1) | (df[col2] != value2)]
    
    # Select n random pairs of columns
    columns = df.columns.tolist()
    pairs = sample(list(zip(columns, columns)), n_plots)
    
    # Create pairplots for the selected pairs
    pairplot_list = []
    for col1, col2 in pairs:
        pairplot = sns.pairplot(df, x_vars=[col1], y_vars=[col2])
        pairplot_list.append(pairplot)
    
    return df, pairplot_list

    # Define tuples to remove rows
    tuples_to_remove = [('A', 'B', 1, 5), ('C', 'D', 2, 6)]
    
    # Generate pairplots for 2 random pairs of columns
    modified_df, pairplots = task_func(df, tuples_to_remove, 2)
    
    # Display the modified DataFrame
    print("Modified DataFrame:")
    print(modified_df)
    
    # Display the pairplots
    for pairplot in pairplots:
        plt.show()