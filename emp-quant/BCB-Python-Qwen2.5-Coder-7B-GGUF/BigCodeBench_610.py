
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
    tuples (list): A list of tuples, each containing two values to be used for filtering the DataFrame.
    n_plots (int): The number of random joint plots to create.
    
    Returns:
    tuple: A tuple containing:
        DataFrame: The modified DataFrame.
        list: A list of generated joint plots (sns.JointGrid objects) if the DataFrame is not empty, otherwise an empty list.
    """
    # Remove rows based on the tuples
    for col1, col2 in tuples:
        df = df[(df[col1] != col2[0]) | (df[col2] != col2[1])]
    
    # Create joint plots if the DataFrame is not empty
    joint_plots = []
    if not df.empty:
        columns = sample(COLUMNS, 2)
        for _ in range(n_plots):
            joint_plot = sns.jointplot(x=columns[0], y=columns[1], data=df)
            joint_plots.append(joint_plot)
    
    return df, joint_plots