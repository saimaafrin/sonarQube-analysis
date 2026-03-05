
from random import sample
import matplotlib.pyplot as plt
import pandas as pd

# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def task_func(df, tuples, n_plots):
    """
    Removes rows from a DataFrame based on values of multiple columns, and then create n random line plots of two columns against each other.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame.
    tuples (list of tuples): A list of tuples, each containing two column names to be used for plotting.
    n_plots (int): The number of random line plots to create.
    
    Returns:
    (pd.DataFrame, list): A tuple containing the modified DataFrame and a list of plot details.
    Each entry in the plot details list is a tuple containing the two columns plotted against each other.
    """
    # Remove rows based on the values of multiple columns
    for col1, col2 in tuples:
        df = df[(df[col1] != 0) & (df[col2] != 0)]
    
    # Create n random line plots
    plot_details = []
    for _ in range(n_plots):
        col1, col2 = sample(COLUMNS, 2)
        plt.figure()
        plt.plot(df[col1], df[col2], marker='o')
        plt.xlabel(col1)
        plt.ylabel(col2)
        plt.title(f'Line Plot of {col1} vs {col2}')
        plt.show()
        plot_details.append((col1, col2))
    
    return df, plot_details

    # Define the tuples of columns to remove rows based on
    tuples_to_remove = [('A', 'B'), ('C', 'D')]
    
    # Number of plots to create
    n_plots = 2
    
    # Call the function
    modified_df, plot_details = task_func(df, tuples_to_remove, n_plots)
    
    # Print the modified DataFrame and plot details
    print("Modified DataFrame:")
    print(modified_df)
    print("Plot Details:")
    print(plot_details)