
from random import sample
import seaborn as sns
import pandas as pd

# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def task_func(df: pd.DataFrame, tuples: list, n_plots: int) -> (pd.DataFrame, list):
    """
    Removes rows from a dataframe based on values of multiple columns, and then creates n random joint plots of two columns against each other.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    tuples (list): A list of tuples where each tuple contains three elements: column name, value to remove, and another value to compare.
    n_plots (int): The number of random joint plots to generate.

    Returns:
    tuple: A tuple containing:
        DataFrame: The modified DataFrame.
        list: A list of generated joint plots (sns.JointGrid objects) if the DataFrame is not empty, otherwise an empty list.
    """
    # Remove rows based on the given conditions
    for col, val1, val2 in tuples:
        df = df[(df[col] != val1) | (df[col] == val2)]
    
    # Check if the DataFrame is not empty
    if not df.empty:
        # Generate n random joint plots
        plot_list = []
        cols = COLUMNS[:len(COLUMNS)-1]  # Exclude the last column for simplicity
        for _ in range(n_plots):
            x_col, y_col = sample(cols, 2)
            plot = sns.jointplot(x=x_col, y=y_col, data=df)
            plot_list.append(plot)
        
        return df, plot_list
    else:
        return df, []