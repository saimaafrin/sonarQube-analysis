from random import sample
import matplotlib.pyplot as plt
import pandas as pd
COLUMNS = ['A', 'B', 'C', 'D', 'E']
def task_func(df, tuples, n_plots):
    """
    Removes rows from a DataFrame based on values of multiple columns, and then creates n random line plots of two columns against each other.
    
    Parameters:
    - df (pd.DataFrame): The input DataFrame.
    - tuples (list of tuples): A list of tuples, each containing two column names to be used for plotting.
    - n_plots (int): The number of random line plots to create.
    
    Returns:
    - (pd.DataFrame, list): A tuple containing the modified DataFrame and a list of plot details.
    Each entry in the plot details list is a tuple containing the two columns plotted against each other.
    """
    # Remove rows based on the tuples
    for col1, col2 in tuples:
        df = df[(df[col1] != df[col2])]
    
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