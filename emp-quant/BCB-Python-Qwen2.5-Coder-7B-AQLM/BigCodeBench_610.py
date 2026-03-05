
from random import sample
import seaborn as sns
import pandas as pd

# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def task_func(df: pd.DataFrame, tuples: list, n_plots: int) -> (pd.DataFrame, list):
    """
    Removes rows from a dataframe based on values of multiple columns, and then creates n random joint plots of two columns against each other if the DataFrame is not empty.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame.
    tuples (list): A list of tuples, each containing three elements: the column name, the value to remove, and the column name to compare with.
    n_plots (int): The number of random joint plots to create if the DataFrame is not empty.
    
    Returns:
    tuple: A tuple containing:
    DataFrame: The modified DataFrame.
    list: A list of generated joint plots (sns.JointGrid objects) if the DataFrame is not empty, otherwise an empty list.
    """
    # Remove rows based on the tuples
    for col, value, compare_col in tuples:
        df = df[(df[col] != value) | (df[compare_col] != value)]
    
    # Create n random joint plots if the DataFrame is not empty
    joint_plots = []
    if not df.empty:
        columns = df.columns.tolist()
        for _ in range(n_plots):
            col1, col2 = sample(columns, 2)
            joint_plot = sns.jointplot(data=df, x=col1, y=col2)
            joint_plots.append(joint_plot)
    
    return df, joint_plots