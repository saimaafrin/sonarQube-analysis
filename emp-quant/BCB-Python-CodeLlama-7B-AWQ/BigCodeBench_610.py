from random import sample
import seaborn as sns
import pandas as pd
import pytest
COLUMNS = ['A', 'B', 'C', 'D', 'E']
def task_func(df: pd.DataFrame, tuples: list, n_plots: int) -> (pd.DataFrame, list):
    """
    Remove rows from a dataframe based on values of multiple columns, and then create n random joint plots of two columns against each other if the DataFrame is not empty.
    The function should output with:
        tuple: A tuple containing:
        DataFrame: The modified DataFrame.
        list: A list of generated joint plots (sns.JointGrid objects) if the DataFrame is not empty, otherwise an empty list.
    """
    # Remove rows from the dataframe based on the values of the specified columns
    for col, val in tuples:
        df = df[df[col] != val]

    # Create n random joint plots of two columns against each other if the DataFrame is not empty
    if not df.empty:
        joint_plots = []
        for _ in range(n_plots):
            col1, col2 = sample(COLUMNS, 2)
            joint_plots.append(sns.JointGrid(col1, col2, data=df))
        return df, joint_plots
    else:
        return df, []