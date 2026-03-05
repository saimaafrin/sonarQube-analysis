
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
    tuples (list of tuples): A list of tuples where each tuple contains the column names to be used for filtering.
    n_plots (int): The number of random line plots to create.
    
    Returns:
    (pd.DataFrame, list): A tuple containing the modified DataFrame and a list of plot details.
    Each entry in the plot details list is a tuple containing the two columns plotted against each other.
    """
    # Filter rows based on the tuples
    for col1, col2 in tuples:
        df = df[(df[col1] != 0) & (df[col2] != 0)]
    
    # Create n random line plots
    plot_details = []
    for _ in range(n_plots):
        cols = sample(COLUMNS, 2)
        plt.figure()
        plt.plot(df[cols[0]], df[cols[1]])
        plt.xlabel(cols[0])
        plt.ylabel(cols[1])
        plt.title(f'Plot of {cols[0]} vs {cols[1]}')
        plt.show()
        plot_details.append((cols[0], cols[1]))
    
    return df, plot_details

    # Define the tuples for filtering
    tuples = [('A', 'B'), ('C', 'D')]
    
    # Call the function
    modified_df, plot_details = task_func(df, tuples, 2)
    
    # Print the modified DataFrame and plot details
    print("Modified DataFrame:")
    print(modified_df)
    print("Plot Details:")
    print(plot_details)