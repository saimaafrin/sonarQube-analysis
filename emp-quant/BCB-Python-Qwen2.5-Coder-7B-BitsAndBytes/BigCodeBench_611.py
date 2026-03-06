
from random import sample
import matplotlib.pyplot as plt
import pandas as pd

# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def task_func(df, tuples, n_plots):
    """
    Removes rows from a DataFrame based on values of multiple columns, and then creates n random line plots of two columns against each other.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    tuples (list of tuples): List of tuples where each tuple contains column names to be used for filtering.
    n_plots (int): Number of random line plots to create.

    Returns:
    (pd.DataFrame, list): A tuple containing the modified DataFrame and a list of plot details.
    Each entry in the plot details list is a tuple containing the two columns plotted against each other.
    """
    # Filter the DataFrame based on the given tuples
    filtered_df = df.copy()
    for col1, col2 in tuples:
        if col1 in COLUMNS and col2 in COLUMNS:
            filtered_df = filtered_df[(filtered_df[col1] != 0) & (filtered_df[col2] != 0)]
    
    # Create n random line plots
    plot_details = []
    for _ in range(n_plots):
        cols_to_plot = sample(COLUMNS, 2)
        plot_details.append(cols_to_plot)
        plt.figure(figsize=(8, 6))
        plt.plot(filtered_df[cols_to_plot[0]], filtered_df[cols_to_plot[1]])
        plt.xlabel(cols_to_plot[0])
        plt.ylabel(cols_to_plot[1])
        plt.title(f'Line Plot of {cols_to_plot[0]} vs {cols_to_plot[1]}')
        plt.show()
    
    return filtered_df, plot_details

    # Tuples to filter
    filter_tuples = [('A', 'B'), ('C', 'D')]
    
    # Number of plots
    num_plots = 2
    
    # Call the function
    result_df, plot_details = task_func(df, filter_tuples, num_plots)
    
    print("Filtered DataFrame:")
    print(result_df)
    print("\nPlot Details:")
    for detail in plot_details:
        print(detail)