from random import sample
import seaborn as sns
import pandas as pd
COLUMNS = ['A', 'B', 'C', 'D', 'E']
def task_func(df: pd.DataFrame, tuples: list, n_plots: int) -> (pd.DataFrame, list):
    """
    Removes rows from a dataframe based on values of multiple columns, and then creates n random joint plots of two columns against each other if the DataFrame is not empty.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame.
    tuples (list): A list of tuples, each containing two values to be used for filtering the DataFrame.
    n_plots (int): The number of random joint plots to create if the DataFrame is not empty.
    
    Returns:
    tuple: A tuple containing:
        DataFrame: The modified DataFrame.
        list: A list of generated joint plots (sns.JointGrid objects) if the DataFrame is not empty, otherwise an empty list.
    """
    # Remove rows based on the tuples
    for tup in tuples:
        df = df[(df[COLUMNS[0]] != tup[0]) | (df[COLUMNS[1]] != tup[1])]
    
    # Create n random joint plots if the DataFrame is not empty
    joint_plots = []
    if not df.empty:
        for _ in range(n_plots):
            cols = sample(COLUMNS, 2)
            plot = sns.jointplot(x=cols[0], y=cols[1], data=df)
            joint_plots.append(plot)
    
    return df, joint_plots