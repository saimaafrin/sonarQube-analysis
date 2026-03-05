
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
    df (DataFrame): The input DataFrame.
    tuples (list of tuples): A list of tuples where each tuple contains two column names and a value to filter by.
    n_plots (int): The number of random pairs of columns to generate pairplots for.
    
    Returns:
    tuple: A tuple containing:
        DataFrame: The modified DataFrame after removing specified rows.
        list of Axes: A list containing the generated pairplots.
    """
    # Remove rows based on the specified tuples
    for col1, col2, value in tuples:
        df = df[(df[col1] != value) & (df[col2] != value)]
    
    # Select n random pairs of columns
    selected_columns = sample(COLUMNS, 2*n_plots)
    column_pairs = [(selected_columns[i], selected_columns[i+1]) for i in range(0, 2*n_plots, 2)]
    
    # Create pairplots
    pairplots = []
    for col1, col2 in column_pairs:
        pairplot = sns.pairplot(df, x_vars=[col1], y_vars=[col2])
        pairplots.append(pairplot)
    
    return df, pairplots

    # Define the tuples to filter by
    tuples = [('A', 'B', 3), ('C', 'D', 5)]
    
    # Call the function
    modified_df, pairplots = task_func(df, tuples, 2)
    
    # Print the modified DataFrame
    print("Modified DataFrame:")
    print(modified_df)
    
    # Show the pairplots
    for pairplot in pairplots:
        plt.show()