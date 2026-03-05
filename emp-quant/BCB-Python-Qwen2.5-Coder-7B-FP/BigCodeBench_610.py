from random import sample
import seaborn as sns
import pandas as pd
def task_func(df: pd.DataFrame, tuples: list, n_plots: int) -> (pd.DataFrame, list):
    """
    Removes rows from a dataframe based on values of multiple columns, and then creates n random joint plots of two columns against each other.
    
    Parameters:
    - df (pd.DataFrame): The input DataFrame.
    - tuples (list): A list of tuples, each containing two column names and a value to filter by.
    - n_plots (int): The number of random joint plots to create.
    
    Returns:
    - tuple: A tuple containing:
        - DataFrame: The modified DataFrame.
        - list: A list of generated joint plots (sns.JointGrid objects) if the DataFrame is not empty, otherwise an empty list.
    """
    # Remove rows based on the tuples
    for col1, col2, value in tuples:
        df = df[(df[col1] != value) & (df[col2] != value)]
    
    # Create joint plots if the DataFrame is not empty
    joint_plots = []
    if not df.empty:
        columns = df.columns.tolist()
        for _ in range(n_plots):
            col1, col2 = sample(columns, 2)
            plot = sns.jointplot(x=col1, y=col2, data=df)
            joint_plots.append(plot)
    
    return df, joint_plots