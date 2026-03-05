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
    # Remove rows based on the values of multiple columns
    mask = df[COLUMNS].isin(tuples).any(axis=1)
    df_filtered = df[~mask]
    
    # Create n random line plots of two columns against each other
    plot_details = []
    for _ in range(n_plots):
        cols = sample(COLUMNS, 2)
        plt.figure()
        plt.plot(df_filtered[cols[0]], df_filtered[cols[1]])
        plt.xlabel(cols[0])
        plt.ylabel(cols[1])
        plt.title(f'Plot of {cols[0]} vs {cols[1]}')
        plt.show()
        plot_details.append((cols[0], cols[1]))
    
    return df_filtered, plot_details